from typing import Tuple

from GalacticGladiators.game.tiles.tile import Tile
from GalacticGladiators.game_texts import SENSOR_TILE_DESCRIPTION
from GalacticGladiators.game_texts import SENSOR_TILE_TITLE
from GalacticGladiators.sprite_locations import TILE_SENSOR_SPRITE


class Sensor(Tile):
    def __init__(self, position: Tuple[int, int]) -> None:
        super().__init__(position, TILE_SENSOR_SPRITE, title=SENSOR_TILE_TITLE, description=SENSOR_TILE_DESCRIPTION)

    def tick(self) -> None:
        super().tick()
        if self.unit:
            self.unit.hidden = False

    def __setstate__(self, state):
        super().__setstate__(state)
        self.set_sprite(TILE_SENSOR_SPRITE)
