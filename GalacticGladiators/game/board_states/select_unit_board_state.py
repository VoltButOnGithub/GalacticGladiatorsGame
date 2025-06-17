import random

from GalacticGladiators.game.board_states.board_state import BoardState
from GalacticGladiators.game.board_states.select_move_board_state import SelectMoveBoardState
from GalacticGladiators.game.utils.board_utils import find_tile_at_point


class SelectUnitBoardState(BoardState):
    def __init__(self, board: 'Board'):
        super().__init__(board)
        self.set_tiles_with_units_clickable(True)
        self.clear_possible_moves()
        self.clear_selected_tile()

    def do_ai_move(self) -> bool:
        if len(self.board.tiles_with_units) == 0:
            self.board.game.finish()
            return True
        random.shuffle(self.board.tiles_with_units)
        self.board.state = SelectMoveBoardState(self.board, self.board.tiles_with_units[0])
        return False

    def on_mouse_click(self, x: int, y: int) -> None:
        if len(self.board.tiles_with_units) == 0:
            self.board.game.finish()
            return
        tile = find_tile_at_point(x, y, self.board.tiles_with_units)
        if tile:
            self.board.state = SelectMoveBoardState(self.board, tile)
