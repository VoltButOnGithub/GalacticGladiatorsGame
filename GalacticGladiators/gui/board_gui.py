import arcade

from GalacticGladiators.game.board import Board
from GalacticGladiators.game.player import Player
from GalacticGladiators.gui.die_gui import draw_die
from GalacticGladiators.gui.fight_gui import draw_fight
from GalacticGladiators.gui.tile_gui import draw_tile_overlay, draw_tile
from GalacticGladiators.gui.unit_gui import draw_currently_placing_unit
from GalacticGladiators.gui.utils.text_draw_utils import draw_text
from GalacticGladiators.settings import GRID_OFFSET_X, GRID_OFFSET_Y


def draw_board(board: Board, client_player: Player) -> None:
    for row in board.tiles:
        for tile in row:
            draw_tile(tile, client_player)
    for row in board.tiles:
        for tile in row:
            draw_tile_overlay(tile, client_player)

    if board.current_unit_to_place:
        draw_currently_placing_unit(board.current_unit_to_place, client_player,
                                    (GRID_OFFSET_X - 100, GRID_OFFSET_Y + 100))

    if board.current_fight:
        draw_fight(board.current_fight, client_player)
    if board.current_die:
        draw_die(board.current_die, client_player)
    if board.current_popup:
        arcade.draw_rectangle_filled(GRID_OFFSET_X + 320, GRID_OFFSET_Y + 320, width=554, height=54,
                                     color=arcade.color.BLACK)
        arcade.draw_rectangle_filled(GRID_OFFSET_X + 320, GRID_OFFSET_Y + 320, width=550, height=50,
                                     color=arcade.color.WINE)
        draw_text(board.current_popup, (GRID_OFFSET_X + 80, GRID_OFFSET_Y + 320))
