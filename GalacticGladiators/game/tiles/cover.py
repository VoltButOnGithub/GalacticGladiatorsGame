from typing import Tuple

from GalacticGladiators.game.tiles.tile import Tile
from GalacticGladiators.game_texts import COVER_TILE_DESCRIPTION
from GalacticGladiators.game_texts import COVER_TILE_TITLE
from GalacticGladiators.sprite_locations import TILE_COVER_SPRITE


class Cover(Tile):
    def __init__(self, position: Tuple[int, int]) -> None:
        super().__init__(position, TILE_COVER_SPRITE, title=COVER_TILE_TITLE, description=COVER_TILE_DESCRIPTION)

    def on_enter(self) -> None:
        self.unit.immune = True

    def on_exit(self) -> None:
        self.unit.immune = False

    def tick(self) -> None:
        super().tick()
        if self.unit:
            self.unit.immune = True

    def __setstate__(self, state):
        super().__setstate__(state)
        self.set_sprite(TILE_COVER_SPRITE)
