from abc import ABC
from typing import Tuple

from arcade import Sprite

from GalacticGladiators.game.units.unit import Unit
from GalacticGladiators.game_texts import GRASS_TILE_DESCRIPTION
from GalacticGladiators.game_texts import GRASS_TILE_TITLE
from GalacticGladiators.settings import GRID_OFFSET_X, GRID_OFFSET_Y
from GalacticGladiators.sprite_locations import TILE_GRASS_SPRITE


class Tile(ABC):
    def __init__(self,
                 position: Tuple[int, int],
                 sprite_location: str = TILE_GRASS_SPRITE,
                 title: str = GRASS_TILE_TITLE,
                 description: str = GRASS_TILE_DESCRIPTION) -> None:
        self.sprite = None
        self.position: Tuple[int, int] = position
        self.unit: Unit | None = None
        self.set_sprite(sprite_location)
        self.title: str = title
        self.description: str = description
        self.hovered: bool = False
        self.selected: bool = False
        self.selectable: bool = False
        self.clickable: bool = False

    def tick(self) -> None:
        if self.unit:
            self.unit.tick()

    def is_passable(self, unit: Unit) -> bool:
        return self.unit is None or self.unit.is_passable(unit)

    def set_unit(self, unit: Unit) -> None:
        self.unit = unit
        self.unit.position = self.position
        self.on_enter()

    def remove_unit(self) -> None:
        self.on_exit()
        self.unit = None

    def on_enter(self) -> None:
        pass

    def on_exit(self) -> None:
        pass

    def has_unit_of_player(self, player: 'Player'):
        return self.unit and self.unit.is_owned_by(player)

    def set_sprite(self, filename: str):
        self.sprite = Sprite(filename=filename)
        self.sprite.center_x = (self.position[0] * 64) + (64 / 2) + GRID_OFFSET_X
        self.sprite.center_y = (self.position[1] * 64) + (64 / 2) + GRID_OFFSET_Y

    def __getstate__(self):
        state = self.__dict__.copy()
        state.pop('sprite')
        return state

    def __setstate__(self, state):
        self.__dict__.update(state)
        self.set_sprite(TILE_GRASS_SPRITE)
