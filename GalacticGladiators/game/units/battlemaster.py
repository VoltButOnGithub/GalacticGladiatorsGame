from typing import Tuple

from arcade import Sprite

from GalacticGladiators.game.board_states.select_unit_board_state import SelectUnitBoardState
from GalacticGladiators.game.player import Player
from GalacticGladiators.game.units.unit import Unit
from GalacticGladiators.game.utils.board_utils import get_friendly_neighbours_of_tile
from GalacticGladiators.game_texts import BATTLEMASTER_UNIT_TITLE, BATTLEMASTER_UNIT_SPECIAL_TITLE, \
    BATTLEMASTER_UNIT_SPECIAL_DESCRIPTION
from GalacticGladiators.sprite_locations import UNIT_BATTLEMASTER_SPRITE


class BattleMaster(Unit):
    def __init__(self, player: Player, pos: Tuple[int, int] = None) -> None:
        super().__init__(player, pos=pos, rank=5,
                         sprite_location=UNIT_BATTLEMASTER_SPRITE,
                         title=BATTLEMASTER_UNIT_TITLE,
                         special_title=BATTLEMASTER_UNIT_SPECIAL_TITLE,
                         special_description=BATTLEMASTER_UNIT_SPECIAL_DESCRIPTION)

    def use_special(self, board: 'Board') -> bool:
        friendly_neighbours = get_friendly_neighbours_of_tile(board.tiles, board.get_tile_at_pos(self.position))
        if len(friendly_neighbours) == 0:
            board.state = SelectUnitBoardState(board)
            return False
        for tile in friendly_neighbours:
            tile.unit.rank_boost_for_ticks(1, 3)
        return True

    def __setstate__(self, state):
        super().__setstate__(state)
        self.sprite = Sprite(UNIT_BATTLEMASTER_SPRITE)
