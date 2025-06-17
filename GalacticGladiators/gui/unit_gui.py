from typing import Tuple

import arcade.color
from arcade import draw_circle_filled

from GalacticGladiators.game.player import Player
from GalacticGladiators.game.units.unit import Unit
from GalacticGladiators.game_texts import RANK, SPECIAL, IMMUNE, AUTO_WIN, CURRENTLY_PLACING
from GalacticGladiators.gui.utils.sprite_draw_utils import draw_offset
from GalacticGladiators.gui.utils.text_draw_utils import draw_text, draw_small_text


def draw_unit(unit: Unit, client_player: Player, pos: Tuple[int, int]) -> None:
    draw_unit_outline(unit, client_player, pos)
    draw_unit_circle(pos, unit)
    if not unit.is_hidden_for(client_player):
        draw_offset(unit.sprite, offset=(pos[0], pos[1]))


def draw_fighting_unit(unit: Unit, client_player: Player, pos: Tuple[int, int]) -> None:
    draw_unit_outline(unit, client_player, pos, show_special=True)
    draw_unit_circle(pos, unit)
    if not unit.is_hidden_for(client_player):
        draw_offset(unit.sprite, offset=(pos[0], pos[1]))
        draw_text(f"{RANK}: {unit.rank}{' + ' + str(unit.rank_boost) if unit.rank_boost > 0 else ''}",
                  (pos[0] - 50, pos[1] - 50))
        if unit.auto_win_defense:
            draw_text(f"({AUTO_WIN})", (pos[0] - 45, pos[1] - 80))


def draw_currently_placing_unit(unit: Unit, client_player: Player, pos: Tuple[int, int]) -> None:
    draw_text(f"{CURRENTLY_PLACING}", (pos[0] - 50, pos[1] + +60))
    draw_text(f"{unit.title}", (pos[0] - 50, pos[1] + 40))

    draw_unit_outline(unit, client_player, pos, show_special=True)
    draw_unit_circle(pos, unit)
    draw_offset(unit.sprite, offset=(pos[0], pos[1]))
    draw_text(f"{RANK}: {unit.rank}", (pos[0] - 50, pos[1] - 50))
    draw_small_text(f"{SPECIAL}: {unit.special_title}", offset=(pos[0] - 50, pos[1] - 70), width=396)


def draw_unit_overlay(pos: Tuple[int, int], unit: Unit, client_player: Player):
    if unit.is_hidden_for(client_player):
        return
    arcade.draw_rectangle_filled(pos[0] + 200 + 32, pos[1] - 18, width=400, height=100, color=arcade.color.BLACK_BEAN)
    draw_text(f"{unit.title} ({RANK}: {unit.rank}{' + ' + str(unit.rank_boost) if unit.rank_boost > 0 else ''})"
              f"{'(' + IMMUNE + ')' if unit.immune else ''}",
              offset=(pos[0] + 32 + 5, pos[1] + 10))
    draw_small_text(f"{SPECIAL}: {unit.special_title}", offset=(pos[0] + 32 + 5, pos[1] - 10), width=396)
    if unit.special_description:
        draw_small_text(unit.special_description, offset=(pos[0] + 32 + 5, pos[1] - 30), width=396)


def draw_unit_outline(unit: Unit, client_player: Player, pos: Tuple[int, int], show_special=False) -> None:
    draw_circle_filled(center_x=pos[0], center_y=pos[1],
                       color=arcade.color.BLACK, radius=28)
    if show_special or unit.is_owned_by(client_player) or unit.cheat_reveal:
        if unit.special_active:
            draw_circle_filled(center_x=pos[0], center_y=pos[1],
                               color=arcade.color.GOLD, radius=28)
        elif unit.rank_boost > 0:
            draw_circle_filled(center_x=pos[0], center_y=pos[1],
                               color=arcade.color.GREEN_YELLOW, radius=28)
        elif unit.immune:
            draw_circle_filled(center_x=pos[0], center_y=pos[1],
                               color=arcade.color.BABY_BLUE, radius=28)


def draw_unit_circle(pos, unit):
    draw_circle_filled(center_x=pos[0], center_y=pos[1],
                       color=unit.player.color, radius=25)
