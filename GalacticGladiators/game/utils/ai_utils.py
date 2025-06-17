import random
from typing import List

from GalacticGladiators.game.aiplayer import AIPlayer
from GalacticGladiators.game.tiles.tile import Tile
from GalacticGladiators.game.units.unit import Unit
from GalacticGladiators.game.utils.game_utils import get_list_of_all_units


def ai_place_units(board: 'Board', ai_player: AIPlayer):
    tiles_to_place_units_on: List[Tile] = [tile for row in board.tiles for tile in row[-2:]]
    units_to_place: List[Unit] = get_list_of_all_units(ai_player)
    random.shuffle(units_to_place)
    for i, tile in enumerate(tiles_to_place_units_on):
        if i < len(units_to_place):
            tile.set_unit(units_to_place[i])
