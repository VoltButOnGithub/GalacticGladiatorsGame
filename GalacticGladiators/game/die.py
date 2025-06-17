import random
from typing import Callable

from GalacticGladiators.game.tiles.tile import Tile
from GalacticGladiators.game_texts import THROWING_DIE


class Die:
    def __init__(self, sides: int, callback: Callable[[int], bool], title: str = THROWING_DIE, attacking_tile=None,
                 defending_tile=None) -> None:
        self.sides: int = sides
        self.outcome: int = random.randint(1, sides)
        self.landed: bool = False
        self.callback: Callable = callback
        self.attacking_tile: Tile | None = attacking_tile
        self.defending_tile: Tile | None = defending_tile
        self.title: str = title
        self.outcome_text: str | None = None

    def land(self) -> None:
        self.landed = True
        if self.attacking_tile and self.attacking_tile.unit:
            self.attacking_tile.unit.reveal_for_ticks(3)
        if self.defending_tile and self.defending_tile.unit:
            self.defending_tile.unit.reveal_for_ticks(3)

    def finish(self) -> None:
        self.callback(self.outcome)
