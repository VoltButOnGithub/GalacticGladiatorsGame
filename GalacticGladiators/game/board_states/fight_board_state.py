from GalacticGladiators.game.board_states.board_state import BoardState
from GalacticGladiators.game.board_states.select_unit_board_state import SelectUnitBoardState
from GalacticGladiators.game.utils.board_utils import move_unit


class FightBoardState(BoardState):
    def __init__(self, board: 'Board'):
        super().__init__(board)
        self.board.clear_hovered()
        self.clear_possible_moves()
        self.clear_selected_tile()

    def on_mouse_click(self, x: int, y: int) -> None:
        if self.board.current_fight:
            if self.board.current_fight.progress_fight():
                if self.board.current_fight.attacker_tile is not self.board.current_fight.loser_tile:
                    move_unit(self.board.current_fight.attacker_tile, self.board.current_fight.defender_tile)
                self.board.current_fight = None
                self.board.state = SelectUnitBoardState(self.board)
                self.board.game.on_player_turn()
            return

    def on_mouse_motion(self, x: int, y: int) -> None:
        pass
