import random
from typing import List, Tuple

from GalacticGladiators.game.board_states.board_state import BoardState
from GalacticGladiators.game.board_states.fight_board_state import FightBoardState
from GalacticGladiators.game.board_states.setup_board_state import SetupBoardState
from GalacticGladiators.game.die import Die
from GalacticGladiators.game.fight import Fight
from GalacticGladiators.game.player import Player
from GalacticGladiators.game.tiles.tile import Tile
from GalacticGladiators.game.units.flag import Flag
from GalacticGladiators.game.units.unit import Unit
from GalacticGladiators.game.utils.ai_utils import ai_place_units
from GalacticGladiators.game.utils.board_utils import generate_tiles, move_unit


class Board:
    def __init__(self, game: 'Game', units: List[Unit]) -> None:
        self.game: 'Game' = game
        self.tiles: List[List[Tile]] = generate_tiles()
        self.tiles_with_units: List[Tile] = []
        self.selected_tile: Tile | None = None
        self.possible_moves: List[Tile] = []
        self.state: BoardState = SetupBoardState(self)
        self.current_fight: Fight | None = None
        self.current_die: Die | None = None
        self.current_popup: str | None = None
        random.shuffle(units)
        self.units_to_place: List[Unit] = units
        self.current_unit_to_place: Unit | None = self.units_to_place[0]
        ai_place_units(self, self.game.players[1])

    def place_unit(self, tile: Tile) -> None:
        tile.set_unit(self.units_to_place[0])
        self.units_to_place.pop(0)
        if len(self.units_to_place) == 0:
            self.current_unit_to_place = None
            self.game.start()
            return
        self.current_unit_to_place = self.units_to_place[0]

    def remove_unit(self, tile: Tile) -> None:
        self.units_to_place.append(tile.unit)
        tile.remove_unit()

    def tick(self) -> None:
        for row in self.tiles:
            for tile in row:
                tile.tick()

    def on_mouse_motion(self, x: int, y: int) -> None:
        self.state.on_mouse_motion(x, y)

    def on_mouse_click(self, x: int, y: int) -> None:
        self.state.on_mouse_click(x, y)

    def do_move(self, tile_to_move_to: Tile) -> bool:
        if tile_to_move_to.unit and not tile_to_move_to.unit.is_owned_by(self.selected_tile.unit.player):
            self.do_fight(self.selected_tile, tile_to_move_to)
            return True
        if tile_to_move_to is self.selected_tile:
            if self.selected_tile.unit.use_special(self):
                self.game.on_player_turn()
                return True
            return False
        if tile_to_move_to.unit is None:
            move_unit(self.selected_tile, tile_to_move_to)
            self.game.on_player_turn()
            return True

    def do_ai_turn(self):
        if not self.state.do_ai_move():
            self.do_ai_turn()

    def do_special_move(self, tile_to_special_move_on: Tile) -> None:
        self.selected_tile.unit.special_move_on(tile_to_special_move_on, self)

    def do_fight(self, attacker_tile: Tile, defender_tile: Tile) -> None:
        self.current_fight = Fight(attacker_tile, defender_tile)
        self.state = FightBoardState(self)

    def contains_flag_of_player(self, player: Player) -> bool:
        return any(
            tile.has_unit_of_player(player) and isinstance(tile.unit, Flag) for row in self.tiles for tile in row)

    def decide_clickable_tiles(self, current_player: Player) -> None:
        self.tiles_with_units.clear()
        self.tiles_with_units = [tile for row in self.tiles for tile in row
                                 if tile.has_unit_of_player(current_player) and not isinstance(tile.unit, Flag)]
        for tile in self.tiles_with_units:
            tile.clickable = True

    def get_tile_at_pos(self, pos: Tuple[int, int]):
        return self.tiles[pos[0]][pos[1]]

    def clear_hovered(self):
        for row in self.tiles:
            for tile in row:
                tile.hovered = False

    def __getstate__(self):
        state = self.__dict__.copy()
        state.pop('game')
        state.pop('current_fight')
        state.pop('current_die')
        state.pop('current_popup')
        state.pop('current_unit_to_place')
        return state

    def __setstate__(self, state):
        self.__dict__.update(state)
        if len(self.units_to_place) != 0:
            self.current_unit_to_place = self.units_to_place[0]
        else:
            self.current_unit_to_place = None
        self.current_fight: Fight | None = None
        self.current_die: Die | None = None
        self.current_popup: str | None = None
