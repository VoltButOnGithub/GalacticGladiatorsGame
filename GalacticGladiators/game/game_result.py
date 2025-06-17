from typing import List

from GalacticGladiators.game.player import Player
from GalacticGladiators.game.player_result import PlayerResult


class GameResult:
    def __init__(self, game: 'Game'):
        self.game: 'Game' = game
        self.player_results: List[PlayerResult] = []
        self.calculate_result()
        self.tie: bool = False
        self.winner: Player = self.calculate_winner()

    def calculate_result(self) -> None:
        for player in self.game.players:
            self.player_results.append(PlayerResult(player, self.game))

    def calculate_winner(self) -> Player:
        winner = self.player_results[0]
        score = winner.total_gold_pieces
        self.tie = True
        for player_result in self.player_results[1:]:
            if player_result.total_gold_pieces > winner.total_gold_pieces:
                winner = player_result
            if player_result.total_gold_pieces != score:
                self.tie = False
        return winner.player
