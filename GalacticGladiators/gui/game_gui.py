from GalacticGladiators.game.game import Game
from GalacticGladiators.gui.board_gui import draw_board
from GalacticGladiators.gui.game_result_gui import draw_game_result
from GalacticGladiators.gui.player_gui import draw_player_info
from GalacticGladiators.settings import PLAYER1_OFFSET_X, PLAYER1_OFFSET_Y, PLAYER2_OFFSET_Y, PLAYER2_OFFSET_X


def draw_game(game: Game) -> None:
    draw_board(game.board, game.client_player)
    draw_player_info(player=game.players[0], offset=(PLAYER1_OFFSET_X, PLAYER1_OFFSET_Y),
                     is_current_player=(game.current_player is game.players[0]),
                     draw_gold_amount=(game.result is None))
    draw_player_info(player=game.players[1], offset=(PLAYER2_OFFSET_X, PLAYER2_OFFSET_Y),
                     is_current_player=(game.current_player is game.players[1]),
                     draw_gold_amount=(game.result is None))
    if game.result:
        draw_game_result(game.result)
