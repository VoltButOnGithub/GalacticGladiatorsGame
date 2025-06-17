from typing import Tuple

from arcade import Sprite

from GalacticGladiators.game.player import Player
from GalacticGladiators.game.units.unit import Unit
from GalacticGladiators.game_texts import FLAG_UNIT_TITLE
from GalacticGladiators.sprite_locations import UNIT_FLAG_SPRITE


class Flag(Unit):
    def __init__(self, player: Player, pos: Tuple[int, int] = None) -> None:
        super().__init__(player, pos=pos, rank=0, sprite_location=UNIT_FLAG_SPRITE, title=FLAG_UNIT_TITLE)

    @property
    def is_special_available(self) -> bool:
        return False

    def __setstate__(self, state):
        super().__setstate__(state)
        self.sprite = Sprite(UNIT_FLAG_SPRITE)
