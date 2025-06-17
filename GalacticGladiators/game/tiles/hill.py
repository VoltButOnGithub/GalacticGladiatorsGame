from typing import Tuple

from GalacticGladiators.game.tiles.tile import Tile
from GalacticGladiators.game_texts import HILL_TILE_DESCRIPTION
from GalacticGladiators.game_texts import HILL_TILE_TITLE
from GalacticGladiators.sprite_locations import TILE_HILL_SPRITE


class Hill(Tile):
    def __init__(self, position: Tuple[int, int]) -> None:
        super().__init__(position, TILE_HILL_SPRITE, title=HILL_TILE_TITLE, description=HILL_TILE_DESCRIPTION)

    def on_enter(self) -> None:
        self.unit.rank_boost += 1

    def on_exit(self) -> None:
        self.unit.rank_boost -= 1

    def __setstate__(self, state):
        super().__setstate__(state)
        self.set_sprite(TILE_HILL_SPRITE)
