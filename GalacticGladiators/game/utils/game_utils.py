from typing import List

from GalacticGladiators.game.player import Player
from GalacticGladiators.game.units.battlemaster import BattleMaster
from GalacticGladiators.game.units.commander import Commander
from GalacticGladiators.game.units.flag import Flag
from GalacticGladiators.game.units.scout import Scout
from GalacticGladiators.game.units.shield_bearer import ShieldBearer
from GalacticGladiators.game.units.sniper import Sniper
from GalacticGladiators.game.units.soldier import Soldier
from GalacticGladiators.game.units.unit import Unit
from GalacticGladiators.settings import SCOUT_AMOUNT, BATTLE_MASTER_AMOUNT, SHIELD_BEARER_AMOUNT, SNIPER_AMOUNT, \
    SOLDIER_AMOUNT, COMMANDER_AMOUNT, FLAG_AMOUNT


def get_list_of_all_units(player: Player) -> List[Unit]:
    list_of_all_units = []
    unit_amounts = {
        Scout: SCOUT_AMOUNT,
        Soldier: SOLDIER_AMOUNT,
        Sniper: SNIPER_AMOUNT,
        ShieldBearer: SHIELD_BEARER_AMOUNT,
        BattleMaster: BATTLE_MASTER_AMOUNT,
        Commander: COMMANDER_AMOUNT,
        Flag: FLAG_AMOUNT
    }
    for unit_class, amount in unit_amounts.items():
        list_of_all_units.extend(unit_class(player) for _ in range(amount))
    return list_of_all_units
