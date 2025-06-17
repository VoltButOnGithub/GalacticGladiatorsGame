from typing import Tuple

from arcade import Sprite

from GalacticGladiators.game.player import Player
from GalacticGladiators.game.units.unit import Unit
from GalacticGladiators.game_texts import SHIELD_BEARER_UNIT_TITLE, SHIELD_BEARER_UNIT_SPECIAL_TITLE, \
    SHIELD_BEARER_UNIT_SPECIAL_DESCRIPTION
from GalacticGladiators.sprite_locations import UNIT_SHIELD_BEARER_SPRITE


class ShieldBearer(Unit):
    def __init__(self, player: Player, pos: Tuple[int, int] = None) -> None:
        super().__init__(player, pos=pos, rank=4, sprite_location=UNIT_SHIELD_BEARER_SPRITE,
                         title=SHIELD_BEARER_UNIT_TITLE,
                         special_title=SHIELD_BEARER_UNIT_SPECIAL_TITLE,
                         special_description=SHIELD_BEARER_UNIT_SPECIAL_DESCRIPTION)
        self.counter = 7

    def use_special(self, board: 'Board') -> bool:
        self.special_active = True
        self.special_used = True
        self.immune = True
        return True

    def tick(self):
        super().tick()
        if self.special_active:
            self.counter -= 1
            if self.counter <= 0:
                self.immune = False
                self.special_active = False

    def __setstate__(self, state):
        super().__setstate__(state)
        self.sprite = Sprite(UNIT_SHIELD_BEARER_SPRITE)
