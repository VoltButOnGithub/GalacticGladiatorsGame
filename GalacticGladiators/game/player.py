from typing import Tuple

from arcade.sprite import Sprite

from GalacticGladiators.sprite_locations import PLAYER_ICON


class Player:
    def __init__(self, name: str, color: Tuple[int, int, int], player_id: int) -> None:
        self.name: str = name
        self.id: int = player_id
        self.gold_pieces: int = 0
        self.sprite: Sprite = Sprite(filename=PLAYER_ICON)
        self.color: Tuple[int, int, int] = color

    def __getstate__(self):
        state = self.__dict__.copy()
        state.pop('sprite')
        return state

    def __setstate__(self, state):
        self.__dict__.update(state)
        self.sprite: Sprite = Sprite(filename=PLAYER_ICON)
