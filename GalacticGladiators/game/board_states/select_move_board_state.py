import random

from GalacticGladiators.game.board_states.board_state import BoardState
from GalacticGladiators.game.tiles.tile import Tile
from GalacticGladiators.game.utils.board_utils import get_passable_neighbours_of_tile, find_tile_at_point
from GalacticGladiators.settings import CPU_SPECIAL_CHANCE


class SelectMoveBoardState(BoardState):
    def __init__(self, board: 'Board', tile: Tile):
        super().__init__(board)
        self.set_selected_tile(tile)
        self.set_possible_moves(get_passable_neighbours_of_tile(self.board.tiles, tile))
        if self.board.selected_tile.unit.is_special_available:
            self.board.selected_tile.selectable = True
            self.board.possible_moves.append(self.board.selected_tile)
        self.set_tiles_with_units_clickable(False)

    def do_ai_move(self) -> bool:
        if len(self.board.possible_moves) == 0:
            from GalacticGladiators.game.board_states.select_unit_board_state import SelectUnitBoardState
            self.board.tiles_with_units.remove(self.board.selected_tile)
            self.board.state = SelectUnitBoardState(self.board)
            return False
        random_number = random.randint(1, 100)
        if (random_number <= CPU_SPECIAL_CHANCE) and self.board.selected_tile.selectable:
            return self.board.do_move(self.board.possible_moves[-1])
        random.shuffle(self.board.possible_moves)
        return self.board.do_move(self.board.possible_moves[0])

    def on_mouse_click(self, x: int, y: int) -> None:
        tile = find_tile_at_point(x, y, self.board.possible_moves)
        if tile:
            self.board.do_move(tile)
            return
        from GalacticGladiators.game.board_states.select_unit_board_state import SelectUnitBoardState
        self.board.state = SelectUnitBoardState(self.board)
