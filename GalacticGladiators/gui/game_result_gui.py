from typing import Tuple

import arcade

from GalacticGladiators.game.game_result import GameResult
from GalacticGladiators.game.player import Player
from GalacticGladiators.game.player_result import PlayerResult
from GalacticGladiators.game_texts import WINS, TIE
from GalacticGladiators.gui.utils.text_draw_utils import draw_text
from GalacticGladiators.settings import PLAYER1_OFFSET_X, PLAYER1_OFFSET_Y, PLAYER2_OFFSET_Y, PLAYER2_OFFSET_X, \
    GRID_OFFSET_Y, GRID_OFFSET_X


def draw_game_result(result: GameResult) -> None:
    draw_player_result(result.player_results[0], (PLAYER1_OFFSET_X, PLAYER1_OFFSET_Y))
    draw_player_result(result.player_results[1], (PLAYER2_OFFSET_X, PLAYER2_OFFSET_Y))
    if result.tie:
        draw_tie()
    else:
        draw_winner(result.winner)


def draw_player_result(player_result: PlayerResult, offset: Tuple[int, int]) -> None:
    draw_text(
        f"{player_result.total_gold_pieces} "
        f"({player_result.player.gold_pieces}"
        f"+{player_result.gold_bonus_pieces}"
        f"{'+' + str(player_result.gold_bonus_flag) if player_result.has_flag else ''}"
        f")",
        (offset[0] + 70, offset[1] - 18))


def draw_winner(winner: Player) -> None:
    arcade.draw_rectangle_filled(GRID_OFFSET_X + 320, GRID_OFFSET_Y + 320, width=304, height=34,
                                 color=arcade.color.BLACK)
    arcade.draw_rectangle_filled(GRID_OFFSET_X + 320, GRID_OFFSET_Y + 320, width=300, height=30,
                                 color=arcade.color.WINE)
    draw_text(winner.name + f" {WINS}", (GRID_OFFSET_X + 200, GRID_OFFSET_Y + 315))


def draw_tie() -> None:
    arcade.draw_rectangle_filled(GRID_OFFSET_X + 320, GRID_OFFSET_Y + 320, width=304, height=34,
                                 color=arcade.color.BLACK)
    arcade.draw_rectangle_filled(GRID_OFFSET_X + 320, GRID_OFFSET_Y + 320, width=300, height=30,
                                 color=arcade.color.WINE)
    draw_text(f"{TIE}", (GRID_OFFSET_X + 200, GRID_OFFSET_Y + 315))
