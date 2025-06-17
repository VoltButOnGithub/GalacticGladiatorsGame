import arcade

from GalacticGladiators.game.fight import Fight
from GalacticGladiators.game.player import Player
from GalacticGladiators.game_texts import FIGHT, VERSUS
from GalacticGladiators.gui.unit_gui import draw_fighting_unit
from GalacticGladiators.gui.utils.text_draw_utils import draw_text
from GalacticGladiators.settings import GRID_OFFSET_X, GRID_OFFSET_Y


def draw_fight(fight: Fight, client_player: Player) -> None:
    arcade.draw_rectangle_filled(GRID_OFFSET_X + 320, GRID_OFFSET_Y + 320, width=260, height=200,
                                 color=arcade.color.BLACK)
    arcade.draw_rectangle_filled(GRID_OFFSET_X + 320, GRID_OFFSET_Y + 320, width=256, height=196,
                                 color=arcade.color.WINE)
    draw_text(FIGHT, (GRID_OFFSET_X + 300, GRID_OFFSET_Y + 380))
    if fight.attacker_tile.unit:
        draw_fighting_unit(fight.attacker_tile.unit, client_player, (GRID_OFFSET_X + 260, GRID_OFFSET_Y + 320))
    draw_text(VERSUS, (GRID_OFFSET_X + 310, GRID_OFFSET_Y + 300))
    if fight.defender_tile.unit:
        draw_fighting_unit(fight.defender_tile.unit, client_player, (GRID_OFFSET_X + 380, GRID_OFFSET_Y + 320))
