from typing import Tuple

from arcade import Sprite

from GalacticGladiators.game.board_states.die_board_state import DieBoardState
from GalacticGladiators.game.board_states.select_special_move_board_state import SelectSpecialMoveBoardState
from GalacticGladiators.game.board_states.select_unit_board_state import SelectUnitBoardState
from GalacticGladiators.game.die import Die
from GalacticGladiators.game.player import Player
from GalacticGladiators.game.units.unit import Unit
from GalacticGladiators.game.utils.board_utils import get_opposing_neighbours_of_tile
from GalacticGladiators.game_texts import SNIPER_UNIT_TITLE, SNIPER_UNIT_SPECIAL_TITLE, SNIPER_UNIT_SPECIAL_DESCRIPTION, \
    SNIPER_ATTEMPT, SNIPER_HIT, SNIPER_MISS, SNIPER_MISS_IMMUNE
from GalacticGladiators.sprite_locations import UNIT_SNIPER_SPRITE


class Sniper(Unit):
    def __init__(self, player: Player, pos: Tuple[int, int] = None) -> None:
        super().__init__(player, pos=pos, rank=3, sprite_location=UNIT_SNIPER_SPRITE,
                         title=SNIPER_UNIT_TITLE,
                         special_title=SNIPER_UNIT_SPECIAL_TITLE,
                         special_description=SNIPER_UNIT_SPECIAL_DESCRIPTION)
        self.tile_to_snipe: 'Tile' = None
        self.board: 'Board' = None

    def use_special(self, board: 'Board') -> bool:
        shootable_tiles = get_opposing_neighbours_of_tile(board.tiles,
                                                          board.get_tile_at_pos(self.position),
                                                          range_to_check=4)
        if len(shootable_tiles) == 0:
            board.state = SelectUnitBoardState(board)
            return False
        board.state = SelectSpecialMoveBoardState(board, board.get_tile_at_pos(self.position),
                                                  shootable_tiles)
        return False

    def special_move_on(self, tile: 'Tile', board: 'Board') -> None:
        board.current_die = Die(6, self.snipe, SNIPER_ATTEMPT, board.get_tile_at_pos(self.position), tile)
        self.hidden = False
        board.state = DieBoardState(board)
        board.current_die.outcome_text = SNIPER_MISS
        if board.current_die.outcome > 4:
            board.current_die.outcome_text = SNIPER_HIT
        if tile.unit.immune:
            board.current_die.outcome_text = SNIPER_MISS_IMMUNE
        self.tile_to_snipe = tile
        self.board = board

    def snipe(self, die_outcome) -> None:
        if die_outcome > 4 and not self.tile_to_snipe.unit.immune:
            self.tile_to_snipe.remove_unit()
        self.board.get_tile_at_pos(self.position).remove_unit()
        self.board.game.on_player_turn()

    def __getstate__(self):
        state = super().__getstate__()
        state.pop('tile_to_snipe')
        state.pop('board')
        return state

    def __setstate__(self, state):
        super().__setstate__(state)
        self.tile_to_snipe = None
        self.board = None
        self.sprite = Sprite(UNIT_SNIPER_SPRITE)
