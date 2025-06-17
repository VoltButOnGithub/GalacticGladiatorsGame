from GalacticGladiators.game.board_states.board_state import BoardState
from GalacticGladiators.game.board_states.select_unit_board_state import SelectUnitBoardState


class PopupBoardState(BoardState):
    def __init__(self, board: 'Board'):
        super().__init__(board)
        self.board.clear_hovered()

    def on_mouse_click(self, x: int, y: int) -> None:
        self.board.current_popup = None
        self.board.state = SelectUnitBoardState(self.board)
        self.board.game.on_player_turn()

    def on_mouse_motion(self, x: int, y: int) -> None:
        pass
