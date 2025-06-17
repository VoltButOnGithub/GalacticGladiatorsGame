from typing import Tuple

from GalacticGladiators.game.tiles.tile import Tile
from GalacticGladiators.game_texts import GOLD_MINE_TILE_DESCRIPTION
from GalacticGladiators.game_texts import GOLD_MINE_TILE_TITLE
from GalacticGladiators.sprite_locations import TILE_GOLDMINE_SPRITE


class GoldMine(Tile):
    def __init__(self, position: Tuple[int, int]) -> None:
        super().__init__(position, TILE_GOLDMINE_SPRITE, title=GOLD_MINE_TILE_TITLE,
                         description=GOLD_MINE_TILE_DESCRIPTION)
        self.counter = 0

    def on_enter(self) -> None:
        self.counter = 0

    def tick(self) -> None:
        super().tick()
        if self.unit:
            self.counter += 1
            if self.counter >= 6:
                self.counter = 0
                self.unit.player.gold_pieces += 1

    def __setstate__(self, state):
        super().__setstate__(state)
        self.set_sprite(TILE_GOLDMINE_SPRITE)
