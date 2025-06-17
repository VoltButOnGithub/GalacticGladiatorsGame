from GalacticGladiators.game.player import Player


class PlayerResult:
    def __init__(self, player: Player, game: 'Game'):
        self.player: Player = player
        self.gold_bonus_pieces: int = self.calculate_gold_bonus_pieces(game)
        self.has_flag: bool = game.board.contains_flag_of_player(player)
        self.gold_bonus_flag: int = 0
        if self.has_flag:
            self.gold_bonus_flag = 10

    def calculate_gold_bonus_pieces(self, game: 'Game') -> int:
        count = 0
        for row in game.board.tiles:
            for tile in row:
                if tile.has_unit_of_player(self.player):
                    count += 1
        return count

    @property
    def total_gold_pieces(self) -> int:
        return self.player.gold_pieces + self.gold_bonus_pieces + self.gold_bonus_flag
