import arcade.color
from arcade import Sprite, draw_circle_filled

from GalacticGladiators.game.player import Player
from GalacticGladiators.game.tiles.tile import Tile
from GalacticGladiators.game_texts import STANDING_ON, GRASS_TILE_TITLE
from GalacticGladiators.gui.unit_gui import draw_unit_overlay, draw_unit
from GalacticGladiators.gui.utils.text_draw_utils import draw_text, draw_small_text
from GalacticGladiators.sprite_locations import SPECIAL_MOVE_ICON


def draw_tile(tile: Tile, client_player: Player) -> None:
    tile.sprite.draw()
    if tile.unit:
        if tile.unit.visible or tile.unit.is_owned_by(client_player) or tile.unit.cheat_reveal:
            draw_unit(tile.unit, client_player, (tile.sprite.center_x.__int__(), tile.sprite.center_y.__int__()))
        if tile.selected and tile.unit.is_special_available and (
                tile.unit.is_owned_by(client_player) or tile.unit.cheat_reveal):
            draw_circle_filled(center_x=tile.sprite.center_x, center_y=tile.sprite.center_y,
                               color=arcade.color.BLACK, radius=28)
            draw_circle_filled(center_x=tile.sprite.center_x, center_y=tile.sprite.center_y,
                               color=arcade.color.YELLOW, radius=25)
            Sprite(SPECIAL_MOVE_ICON, center_x=tile.sprite.center_x, center_y=tile.sprite.center_y).draw()
    if tile.selected:
        arcade.draw_rectangle_filled(tile.sprite.center_x, tile.sprite.center_y, 64, 64, (255, 255, 0, 150))
        return
    if tile.selectable:
        arcade.draw_rectangle_filled(tile.sprite.center_x, tile.sprite.center_y, 64, 64, (255, 0, 0, 150))


def draw_tile_info(pos, title, description, standing_on=False):
    arcade.draw_rectangle_filled(pos[0] + 150 + 32, pos[1] - 10, width=300, height=86, color=arcade.color.BLACK_BEAN)
    draw_text(f"{STANDING_ON + ' ' if standing_on else ''}{title}", offset=(pos[0] + 32 + 5, pos[1] + 10))
    draw_small_text(description, offset=(pos[0] + 32 + 5, pos[1] - 20), width=300)


def draw_tile_overlay(tile: Tile, current_player: Player) -> None:
    if not tile.hovered:
        return
    if tile.title != GRASS_TILE_TITLE:
        if tile.unit is None or tile.unit.is_hidden_for(current_player):
            draw_tile_info((tile.sprite.center_x, tile.sprite.center_y), tile.title, tile.description)
        else:
            draw_tile_info((tile.sprite.center_x, tile.sprite.center_y - 100), tile.title, tile.description,
                           standing_on=True)
    if tile.unit:
        draw_unit_overlay((tile.sprite.center_x, tile.sprite.center_y), tile.unit, current_player)
