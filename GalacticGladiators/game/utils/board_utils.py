import random
from functools import wraps
from typing import List, Callable, Tuple

from GalacticGladiators.game.enums.direction import Direction
from GalacticGladiators.game.tiles.cover import Cover
from GalacticGladiators.game.tiles.gold_mine import GoldMine
from GalacticGladiators.game.tiles.hill import Hill
from GalacticGladiators.game.tiles.sensor import Sensor
from GalacticGladiators.game.tiles.tile import Tile
from GalacticGladiators.settings import BOARD_ROWS, BOARD_COLS, HILL_AMOUNT, COVER_AMOUNT, SENSOR_AMOUNT, \
    GOLD_MINE_AMOUNT


def generate_tiles() -> List[List[Tile]]:
    tiles = [[Tile(position=(x, y)) for y in range(BOARD_COLS)] for x in range(BOARD_ROWS)]
    middle_positions = [(x, y) for x in range(BOARD_ROWS) for y in range(3, 7)]
    random.shuffle(middle_positions)
    tile_amounts = {
        Hill: HILL_AMOUNT,
        Cover: COVER_AMOUNT,
        Sensor: SENSOR_AMOUNT,
        GoldMine: GOLD_MINE_AMOUNT
    }
    start_index = 0
    for tile_class, count in tile_amounts.items():
        positions = middle_positions[start_index:start_index + count]
        for pos in positions:
            x, y = pos
            tiles[x][y] = tile_class(position=pos)
        start_index += count
    return tiles


def move_unit(from_tile: Tile, to_tile: Tile) -> None:
    to_tile.set_unit(from_tile.unit)
    from_tile.remove_unit()


def iterate_neighbours(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(tiles: List[List[Tile]], tile: Tile, range_to_check: int = 1) -> List[Tile]:
        neighbours = []
        for distance in range(1, range_to_check + 1):
            for direction in Direction:
                pos = (
                    tile.position[0] + direction.value[0] * distance,  # x
                    tile.position[1] + direction.value[1] * distance  # y
                )
                if pos_in_bounds(pos, tiles):
                    result = func(tiles, tile, pos)
                    if result:
                        neighbours.append(result)
        return neighbours

    return wrapper


@iterate_neighbours
def get_passable_neighbours_of_tile(tiles: List[List[Tile]], tile: Tile, pos: Tuple[int, int]) -> Tile | None:
    if tiles[pos[0]][pos[1]].is_passable(tile.unit):
        return tiles[pos[0]][pos[1]]
    return None


@iterate_neighbours
def get_friendly_neighbours_of_tile(tiles: List[List[Tile]], tile: Tile, pos: Tuple[int, int]) -> Tile | None:
    if tiles[pos[0]][pos[1]].unit and tiles[pos[0]][pos[1]].unit.is_owned_by(tile.unit.player):
        return tiles[pos[0]][pos[1]]
    return None


@iterate_neighbours
def get_opposing_neighbours_of_tile(tiles: List[List[Tile]], tile: Tile, pos: Tuple[int, int]) -> Tile | None:
    if tiles[pos[0]][pos[1]].unit and not tiles[pos[0]][pos[1]].unit.is_owned_by(tile.unit.player):
        return tiles[pos[0]][pos[1]]
    return None


def pos_in_bounds(pos: Tuple[int, int], list_to_check: List[List]) -> bool:
    if not -1 < pos[0] < len(list_to_check):
        return False
    if not -1 < pos[1] < len(list_to_check[pos[0]]):
        return False
    return True


def find_tile_at_point(x: int, y: int, tiles: List[Tile]) -> Tile:
    for tile in tiles:
        if tile.sprite.collides_with_point((x, y)):
            return tile


def find_tile_at_point_in_grid(x: int, y: int, tiles: List[List[Tile]]) -> Tile:
    for row in tiles:
        for tile in row:
            if tile.sprite.collides_with_point((x, y)):
                return tile
