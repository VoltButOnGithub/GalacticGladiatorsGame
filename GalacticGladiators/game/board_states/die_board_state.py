from GalacticGladiators.game.board_states.board_state import BoardState
from GalacticGladiators.game.board_states.select_unit_board_state import SelectUnitBoardState


class DieBoardState(BoardState):
    def __init__(self, board: 'Board'):
        super().__init__(board)
        self.board.clear_hovered()
        self.clear_possible_moves()
        self.clear_selected_tile()

    def on_mouse_click(self, x: int, y: int) -> None:
        if self.board.current_die:
            if not self.board.current_die.landed:
                self.board.current_die.land()
            else:
                self.board.current_die.finish()
                self.board.current_die = None
                self.board.state = SelectUnitBoardState(self.board)
            return

    def on_mouse_motion(self, x: int, y: int) -> None:
        pass
