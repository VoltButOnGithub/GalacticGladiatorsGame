from typing import Tuple

import arcade

from GalacticGladiators.game.player import Player
from GalacticGladiators.gui.utils.sprite_draw_utils import draw_offset
from GalacticGladiators.gui.utils.text_draw_utils import draw_text
from GalacticGladiators.settings import GOLD_SPRITE


def draw_player_info(player: Player, offset: Tuple[int, int], is_current_player: bool, draw_gold_amount=True) -> None:
    if is_current_player:
        arcade.draw_rectangle_filled(center_x=offset[0], center_y=offset[1],
                                     width=player.sprite.width + 3, height=player.sprite.height + 3,
                                     color=arcade.color.GOLD)
    arcade.draw_rectangle_filled(center_x=offset[0], center_y=offset[1],
                                 width=player.sprite.width, height=player.sprite.height, color=player.color)
    draw_offset(player.sprite, offset)
    draw_text(player.name, (offset[0] + 40, offset[1] + 10))
    draw_offset(GOLD_SPRITE, (offset[0] + 50, offset[1] - 10))
    if draw_gold_amount:
        draw_text(str(player.gold_pieces), (offset[0] + 70, offset[1] - 18))
