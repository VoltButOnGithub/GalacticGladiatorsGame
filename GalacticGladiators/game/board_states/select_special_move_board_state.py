import random
from typing import List

from GalacticGladiators.game.board_states.board_state import BoardState
from GalacticGladiators.game.board_states.select_unit_board_state import SelectUnitBoardState
from GalacticGladiators.game.tiles.tile import Tile
from GalacticGladiators.game.utils.board_utils import find_tile_at_point


class SelectSpecialMoveBoardState(BoardState):
    def __init__(self, board: 'Board', tile: Tile, possible_moves: List[Tile]):
        super().__init__(board)
        self.clear_possible_moves()
        self.set_selected_tile(tile)
        self.set_possible_moves(possible_moves)

    def do_ai_move(self) -> bool:
        if len(self.board.possible_moves) == 0:
            from GalacticGladiators.game.board_states.select_unit_board_state import SelectUnitBoardState
            self.board.state = SelectUnitBoardState(self.board)
            return False
        random.shuffle(self.board.possible_moves)
        self.board.do_special_move(self.board.possible_moves[0])
        return True

    def on_mouse_click(self, x: int, y: int) -> None:
        tile = find_tile_at_point(x, y, self.board.possible_moves)
        if tile:
            self.board.do_special_move(tile)
            return
        self.board.state = SelectUnitBoardState(self.board)
