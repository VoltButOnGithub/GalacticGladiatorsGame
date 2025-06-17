from typing import Tuple

from arcade import Sprite

from GalacticGladiators.game.player import Player
from GalacticGladiators.game.units.unit import Unit
from GalacticGladiators.game_texts import SCOUT_UNIT_TITLE, SCOUT_UNIT_SPECIAL_TITLE, SCOUT_UNIT_SPECIAL_DESCRIPTION
from GalacticGladiators.sprite_locations import UNIT_SCOUT_SPRITE


class Scout(Unit):
    def __init__(self, player: Player, pos: Tuple[int, int] = None):
        super().__init__(player, pos=pos, rank=1, sprite_location=UNIT_SCOUT_SPRITE,
                         title=SCOUT_UNIT_TITLE,
                         special_title=SCOUT_UNIT_SPECIAL_TITLE,
                         special_description=SCOUT_UNIT_SPECIAL_DESCRIPTION)
        self.counter = 7

    def use_special(self, board: 'Board') -> bool:
        self.special_active = True
        self.special_used = True
        self.visible = False
        self.auto_win_defense = True
        return True

    def tick(self):
        super().tick()
        if self.special_active:
            self.counter -= 1
            if self.counter <= 0:
                self.visible = True
                self.special_active = False
                self.auto_win_defense = False

    def __setstate__(self, state):
        super().__setstate__(state)
        self.sprite = Sprite(UNIT_SCOUT_SPRITE)
