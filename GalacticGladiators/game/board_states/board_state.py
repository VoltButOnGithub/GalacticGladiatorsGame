from abc import ABC
from typing import List

from GalacticGladiators.game.tiles.tile import Tile
from GalacticGladiators.game.utils.board_utils import find_tile_at_point_in_grid
from GalacticGladiators.gui.utils.mouse_utils import set_cursor_default, set_cursor_hand


class BoardState(ABC):
    def __init__(self, board: 'Board') -> None:
        self.board = board

    def do_ai_move(self) -> bool:
        return False

    def on_mouse_click(self, x: int, y: int) -> None:
        pass

    def on_mouse_motion(self, x: int, y: int) -> None:
        self.board.clear_hovered()
        tile = find_tile_at_point_in_grid(x, y, self.board.tiles)
        if tile:
            tile.hovered = True
            if tile.clickable:
                set_cursor_hand()
                return
        set_cursor_default()

    def set_selected_tile(self, tile: Tile):
        tile.selected = True
        self.board.selected_tile = tile

    def clear_selected_tile(self):
        if self.board.selected_tile:
            self.board.selected_tile.selected = False
            self.board.selected_tile.selectable = False
            self.board.selected_tile = None

    def set_possible_moves(self, possible_moves: List[Tile]):
        self.board.possible_moves = possible_moves
        for tile in self.board.possible_moves:
            tile.clickable = True
            tile.selectable = True

    def clear_possible_moves(self):
        for tile in self.board.possible_moves:
            tile.selectable = False
            tile.clickable = False
        self.board.possible_moves.clear()

    def set_tiles_with_units_clickable(self, value: bool):
        for tile in self.board.tiles_with_units:
            tile.clickable = value
