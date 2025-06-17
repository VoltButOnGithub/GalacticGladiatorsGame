import arcade.color
from arcade.sprite import Sprite

from sprite_locations import GOLD_ICON

SAVES_DIRECTORY = 'saves/'  # 'saves/'

# SETTINGS FILE
# change values but be wary of stuff breaking
# default values are commented behind value

# Screen stuff
SCREEN_WIDTH: int = 1200  # 1200
SCREEN_HEIGHT: int = 1000  # 1000
SCREEN_TITLE: str = "Galactic Gladiators"  # "Galactic Gladiators"
FPS_LIMIT: float = 60  # 60 (doesnt work)

# Board size
BOARD_ROWS: int = 10  # 10
BOARD_COLS: int = 10  # 10

# Unit amounts
SCOUT_AMOUNT: int = 3  # 3
SOLDIER_AMOUNT: int = 7  # 7
SNIPER_AMOUNT: int = 3  # 3
SHIELD_BEARER_AMOUNT: int = 2  # 2
BATTLE_MASTER_AMOUNT: int = 2  # 2
COMMANDER_AMOUNT: int = 2  # 2
FLAG_AMOUNT: int = 1  # 1

# Special tile amounts
HILL_AMOUNT: int = 3  # 3
COVER_AMOUNT: int = 2  # 2
SENSOR_AMOUNT: int = 4  # 4
GOLD_MINE_AMOUNT: int = 3  # 3

# Offsets and sprites, probably don't touch
GRID_OFFSET_X: int = 300  # 300
GRID_OFFSET_Y: int = 180  # 180
PLAYER1_OFFSET_X: int = 330  # 330
PLAYER1_OFFSET_Y: int = 140  # 140
PLAYER2_OFFSET_X: int = 330  # 330
PLAYER2_OFFSET_Y: int = 860  # 860
GOLD_SPRITE: Sprite = Sprite(GOLD_ICON, scale=0.5)

# colors!!! yippee
PLAYER1_COLOR: (int, int, int) = arcade.color.SPANISH_RED
PLAYER2_COLOR: (int, int, int) = arcade.color.SPANISH_BLUE

# gameplay
# Chance of the CPU player to do a special move on the unit it randomly chose
# if this chance fails, the CPU can still choose the special move out of the possible moves with the unit
CPU_SPECIAL_CHANCE: int = 25  # 50
