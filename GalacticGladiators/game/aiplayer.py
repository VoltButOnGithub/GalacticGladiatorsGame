from arcade.sprite import Sprite

from GalacticGladiators.game.player import Player
from GalacticGladiators.game_texts import CPU_NAME
from GalacticGladiators.sprite_locations import CPU_ICON


class AIPlayer(Player):
    def __init__(self, color: (int, int, int), player_id: int) -> None:
        super().__init__(CPU_NAME, color, player_id)
        self.sprite = Sprite(filename=CPU_ICON)

    def __setstate__(self, state):
        self.__dict__.update(state)
        self.sprite: Sprite = Sprite(filename=CPU_ICON)
