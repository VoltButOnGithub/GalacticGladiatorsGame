from datetime import datetime
from typing import Tuple

from GalacticGladiators.data.save_game import save_game, delete_game
from GalacticGladiators.game.aiplayer import AIPlayer
from GalacticGladiators.game.board import Board
from GalacticGladiators.game.board_states.board_state import BoardState
from GalacticGladiators.game.board_states.finished_board_state import FinishedBoardState
from GalacticGladiators.game.board_states.locked_board_state import LockedBoardState
from GalacticGladiators.game.board_states.select_unit_board_state import SelectUnitBoardState
from GalacticGladiators.game.game_result import GameResult
from GalacticGladiators.game.player import Player
from GalacticGladiators.game.utils.game_utils import get_list_of_all_units
from GalacticGladiators.settings import (PLAYER1_COLOR, PLAYER2_COLOR)


class Game:
    def __init__(self, name: str, app: 'Application') -> None:
        self.players: Tuple[Player, Player] = (Player(name, PLAYER1_COLOR, 0), AIPlayer(PLAYER2_COLOR, 1))
        self.board: Board = Board(self, get_list_of_all_units(self.players[0]))
        self.start_datetime: datetime = datetime.now()
        self.__current_player_index: int = 0
        self.__client_player_index: int = 0
        self.paused: bool = False
        self.last_board_state: BoardState | None = None
        self.cheats_active: bool = False
        self.result: GameResult | None = None
        self.app: 'Application' = app

    def start(self):
        self.board.decide_clickable_tiles(self.current_player)
        self.board.state = SelectUnitBoardState(self.board)
        save_game(self)

    @property
    def current_player(self) -> Player:
        return self.players[self.__current_player_index]

    @property
    def client_player(self) -> Player:
        return self.players[self.__client_player_index]

    def on_mouse_motion(self, x: int, y: int) -> None:
        self.board.on_mouse_motion(x, y)

    def on_mouse_click(self, x: int, y: int) -> None:
        self.board.on_mouse_click(x, y)

    def on_player_turn(self) -> None:
        self.board.tick()
        self.switch_player()
        if not self.board.contains_flag_of_player(self.current_player):
            self.finish()
            return
        self.board.decide_clickable_tiles(self.current_player)
        self.board.state = SelectUnitBoardState(self.board)
        if isinstance(self.current_player, AIPlayer):
            self.board.do_ai_turn()
        save_game(self)

    def finish(self) -> None:
        self.result = GameResult(self)
        self.set_each_unit_cheat_reveal(True)
        self.board.state = FinishedBoardState(self.board)
        self.app.open_finished_game_menu()
        delete_game(self)

    def switch_player(self) -> None:
        self.__current_player_index += 1
        if self.__current_player_index >= len(self.players):
            self.__current_player_index = 0

    def pause(self) -> None:
        self.paused = True
        self.last_board_state = self.board.state
        self.board.state = LockedBoardState(self.board)

    def unpause(self) -> None:
        self.paused = False
        self.board.state = self.last_board_state

    def toggle_cheats(self) -> None:
        if self.cheats_active:
            self.cheats_active = False
            self.set_each_unit_cheat_reveal(False)
        else:
            self.cheats_active = True
            self.set_each_unit_cheat_reveal(True)

    def set_each_unit_cheat_reveal(self, value: bool) -> None:
        for row in self.board.tiles:
            for tile in row:
                if tile.unit:
                    tile.unit.cheat_reveal = value

    def __getstate__(self):
        state = self.__dict__.copy()
        state.pop('last_board_state')
        state.pop('paused')
        state.pop('app')
        return state

    def __setstate__(self, state):
        self.__dict__.update(state)
        self.board.game = self
        self.last_board_state = None
        self.paused = False
        for row in self.board.tiles:
            for tile in row:
                if tile.unit:
                    tile.unit.player = self.players[tile.unit.player_id]
