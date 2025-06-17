from GalacticGladiators.game.player import Player
from GalacticGladiators.game.tiles.tile import Tile


class Fight:
    def __init__(self, attacker_tile: Tile, defender_tile: Tile):
        self.attacker_tile: Tile = attacker_tile
        self.defender_tile: Tile = defender_tile
        self.instigator: Player = attacker_tile.unit.player
        self.loser_tile: Tile = self.get_loser()
        self.stage: int = 0
        if not self.defender_tile.unit.is_hidden_for(self.instigator):
            self.stage = 1
        self.attacker_tile.unit.visible = True
        self.defender_tile.unit.visible = True

    def get_loser(self) -> Tile:
        # Defender has auto win and attacker is not immune, attacker loses
        if self.defender_tile.unit.auto_win_defense and not self.attacker_tile.unit.immune:
            return self.attacker_tile
        # Attackers rank <= defenders rank, attacker loses
        if self.attacker_tile.unit.effective_rank <= self.defender_tile.unit.effective_rank:
            return self.attacker_tile
        else:
            return self.defender_tile

    def progress_fight(self) -> bool:
        self.stage += 1
        match self.stage:
            case 1:
                self.attacker_tile.unit.hidden = False
                self.defender_tile.unit.hidden = False
            case 2:
                self.attacker_tile.unit.reveal_for_ticks(3)
                self.defender_tile.unit.reveal_for_ticks(3)
                self.loser_tile.remove_unit()
            case 3:
                return True
            case _:
                return True
