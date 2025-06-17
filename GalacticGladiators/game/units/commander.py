from typing import Tuple

from arcade import Sprite

from GalacticGladiators.game.board_states.popup_board_state import PopupBoardState
from GalacticGladiators.game.board_states.select_special_move_board_state import SelectSpecialMoveBoardState
from GalacticGladiators.game.board_states.select_unit_board_state import SelectUnitBoardState
from GalacticGladiators.game.player import Player
from GalacticGladiators.game.units.unit import Unit
from GalacticGladiators.game.utils.board_utils import get_opposing_neighbours_of_tile
from GalacticGladiators.game_texts import COMMANDER_UNIT_TITLE, COMMANDER_UNIT_SPECIAL_TITLE, \
    COMMANDER_UNIT_SPECIAL_DESCRIPTION, COMMANDER_FAIL_IMMUNE
from GalacticGladiators.sprite_locations import UNIT_COMMANDER_SPRITE


class Commander(Unit):
    def __init__(self, player: Player, pos: Tuple[int, int] = None):
        super().__init__(player, pos=pos, rank=6, sprite_location=UNIT_COMMANDER_SPRITE,
                         title=COMMANDER_UNIT_TITLE,
                         special_title=COMMANDER_UNIT_SPECIAL_TITLE,
                         special_description=COMMANDER_UNIT_SPECIAL_DESCRIPTION)

    def use_special(self, board: 'Board') -> bool:
        convertable_tiles = get_opposing_neighbours_of_tile(board.tiles, board.get_tile_at_pos(self.position))
        if len(convertable_tiles) == 0:
            board.state = SelectUnitBoardState(board)
            return False
        board.state = SelectSpecialMoveBoardState(board, board.get_tile_at_pos(self.position), convertable_tiles)
        return False

    def special_move_on(self, tile: 'Tile', board: 'Board') -> None:
        if tile.unit.immune:
            board.current_popup = COMMANDER_FAIL_IMMUNE
            board.state = PopupBoardState(board)
            return
        tile.unit.set_player(self.player)
        board.game.on_player_turn()

    def __setstate__(self, state):
        super().__setstate__(state)
        self.sprite = Sprite(UNIT_COMMANDER_SPRITE)
