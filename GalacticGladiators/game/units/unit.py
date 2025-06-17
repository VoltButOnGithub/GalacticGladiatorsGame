from abc import ABC
from typing import List, Tuple

from arcade import Sprite

from GalacticGladiators.game.player import Player


class Unit(ABC):
    def __init__(self, player: Player, rank: int, sprite_location: str, title: str = None, pos: Tuple[int, int] = None,
                 special_title: str = None,
                 special_description: str = None) -> None:
        self.player: Player = player
        self.player_id: int = player.id
        self.rank: int = rank
        self.rank_boost: int = 0
        self.temporary_rank_boosts: List[RankBoost] = []
        self.position: Tuple[int, int] | None = pos
        self.title: str = title
        self.special_title: str = special_title
        self.special_description: str = special_description
        self.special_used: bool = False
        self.special_active: bool = False
        self.hidden: bool = True
        self.ticks_left_revealed: int = 0
        self.cheat_reveal: bool = False
        self.visible: bool = True
        self.immune: bool = False
        self.sprite: Sprite = Sprite(sprite_location)
        self.auto_win_defense: bool = False

    def use_special(self, board: 'Board') -> bool:
        """ :return: True if the units special finishes the turn, False otherwise """
        pass

    def special_move_on(self, tile: 'Tile', board: 'Board') -> None:
        pass

    def reveal_for_ticks(self, ticks: int) -> None:
        self.ticks_left_revealed += ticks
        self.hidden = False

    def rank_boost_for_ticks(self, boost: int, ticks: int) -> None:
        self.rank_boost += boost
        self.temporary_rank_boosts.append(RankBoost(boost, ticks))

    def set_player(self, player: Player):
        self.player = player
        self.player_id = player.id

    def tick(self) -> None:
        self.__tick_reveal_status()
        self.__tick_rank_boosts()

    def __tick_reveal_status(self) -> None:
        if self.ticks_left_revealed > 0:
            self.ticks_left_revealed -= 1
        if self.ticks_left_revealed <= 0:
            self.hidden = True

    def __tick_rank_boosts(self) -> None:
        for rank_boost in self.temporary_rank_boosts:
            rank_boost.ticks_left -= 1
            if rank_boost.ticks_left <= 0:
                self.rank_boost -= rank_boost.boost
                self.temporary_rank_boosts.remove(rank_boost)

    def is_owned_by(self, player: Player) -> bool:
        return self.player is player

    def is_hidden_for(self, player: Player) -> bool:
        if self.is_owned_by(player) or self.cheat_reveal:
            return False
        else:
            return self.hidden

    def is_passable(self, unit: 'Unit') -> bool:
        return unit.player is not self.player

    @property
    def is_special_available(self) -> bool:
        return not self.special_used and not self.special_active

    @property
    def effective_rank(self) -> int:
        return self.rank + self.rank_boost

    def __getstate__(self):
        state = self.__dict__.copy()
        state.pop('sprite')
        state.pop('player')
        return state

    def __setstate__(self, state):
        self.__dict__.update(state)


class RankBoost:
    def __init__(self, boost: int, duration: int):
        self.boost: int = boost
        self.ticks_left: int = duration
