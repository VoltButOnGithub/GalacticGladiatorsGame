from GalacticGladiators.game.board_states.board_state import BoardState


class LockedBoardState(BoardState):
    def __init__(self, board: 'Board'):
        super().__init__(board)
        self.board.clear_hovered()

    def on_mouse_motion(self, x: int, y: int) -> None:
        pass
