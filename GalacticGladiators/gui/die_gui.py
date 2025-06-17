import random

import arcade

from GalacticGladiators.game.die import Die
from GalacticGladiators.game.player import Player
from GalacticGladiators.gui.unit_gui import draw_fighting_unit
from GalacticGladiators.gui.utils.text_draw_utils import draw_text
from GalacticGladiators.settings import GRID_OFFSET_X, GRID_OFFSET_Y


def draw_die(die: Die, client_player: Player) -> None:
    arcade.draw_rectangle_filled(GRID_OFFSET_X + 320, GRID_OFFSET_Y + 320, width=284, height=224,
                                 color=arcade.color.BLACK)
    arcade.draw_rectangle_filled(GRID_OFFSET_X + 320, GRID_OFFSET_Y + 320, width=280, height=220,
                                 color=arcade.color.WINE)

    arcade.draw_rectangle_filled(GRID_OFFSET_X + 320, GRID_OFFSET_Y + 320, width=54, height=54,
                                 color=arcade.color.BLACK)
    arcade.draw_rectangle_filled(GRID_OFFSET_X + 320, GRID_OFFSET_Y + 320, width=50, height=50, color=arcade.color.WINE)
    draw_text(die.title, (GRID_OFFSET_X + 270, GRID_OFFSET_Y + 390))
    if die.attacking_tile and die.attacking_tile.unit:
        draw_fighting_unit(die.attacking_tile.unit, client_player,
                           (GRID_OFFSET_X + 260, GRID_OFFSET_Y + 320))
    if die.defending_tile and die.defending_tile.unit:
        draw_fighting_unit(die.defending_tile.unit, client_player,
                           (GRID_OFFSET_X + 380, GRID_OFFSET_Y + 320))
    if not die.landed:
        draw_text(random.randint(1, die.sides), (GRID_OFFSET_X + 310, GRID_OFFSET_Y + 315))
    if die.landed:
        draw_text(die.outcome, (GRID_OFFSET_X + 310, GRID_OFFSET_Y + 315))
        draw_text(die.outcome_text, (GRID_OFFSET_X + 300, GRID_OFFSET_Y + 260))
