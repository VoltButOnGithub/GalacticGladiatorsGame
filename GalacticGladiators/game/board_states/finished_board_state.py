from GalacticGladiators.game.board_states.board_state import BoardState


class FinishedBoardState(BoardState):
    def __init__(self, board: 'Board'):
        super().__init__(board)
        self.board.clear_hovered()
