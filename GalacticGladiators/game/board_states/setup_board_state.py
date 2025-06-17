from typing import List

from GalacticGladiators.game.board_states.board_state import BoardState
from GalacticGladiators.game.tiles.tile import Tile
from GalacticGladiators.game.utils.board_utils import find_tile_at_point


class SetupBoardState(BoardState):
    def __init__(self, board: 'Board'):
        super().__init__(board)
        self.free_tiles: List[Tile] = [tile for row in board.tiles for tile in row[:2]]
        for tile in self.free_tiles:
            tile.clickable = True
            tile.selectable = True

    def on_mouse_click(self, x: int, y: int) -> None:
        tile = find_tile_at_point(x, y, self.free_tiles)
        if tile:
            if tile and tile.unit:
                self.board.remove_unit(tile)
                tile.selectable = True
            else:
                self.board.place_unit(tile)
                tile.selectable = False
