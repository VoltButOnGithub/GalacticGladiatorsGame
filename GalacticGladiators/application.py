from typing import Any

import arcade
import arcade.gui

from GalacticGladiators.data.save_game import load_game, delete_game_file
from GalacticGladiators.game.game import Game
from GalacticGladiators.game_texts import DEFAULT_PLAYER_NAME
from GalacticGladiators.gui.game_gui import draw_game
from GalacticGladiators.menu.finished_game_menu import FinishedGameMenu
from GalacticGladiators.menu.game_setup_menu import GameSetupMenu
from GalacticGladiators.menu.load_game_menu import LoadGameMenu
from GalacticGladiators.menu.main_menu import MainMenu
from GalacticGladiators.menu.menu import Menu
from GalacticGladiators.menu.pause_menu import PauseMenu
from GalacticGladiators.settings import SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, FPS_LIMIT


class Application(arcade.Window):
    def __init__(self) -> None:
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, update_rate=1 / FPS_LIMIT)

        arcade.set_background_color(arcade.color.ARSENIC)
        self.menu: Menu | None = MainMenu(self)
        self.game: Game | None = None

    def on_draw(self) -> None:
        self.clear()
        arcade.start_render()
        if self.game:
            draw_game(self.game)
        if self.menu:
            self.menu.manager.draw()

    def on_mouse_motion(self, x: int, y: int, delta_x: int, delta_y: int) -> None:
        if self.game:
            self.game.on_mouse_motion(x, y)

    def on_mouse_press(self, x: int, y: int, button: int, key_modifiers: Any) -> None:
        if self.game:
            self.game.on_mouse_click(x, y)

    def on_key_press(self, key, modifiers) -> None:
        if self.game and key == arcade.key.ESCAPE and not isinstance(self.menu, FinishedGameMenu):
            self.toggle_pause()

    def toggle_pause(self) -> None:
        if self.game.paused:
            self.clear_menu()
            self.game.unpause()
        else:
            self.game.pause()
            self.menu = PauseMenu(self)

    def clear_menu(self) -> None:
        self.menu.manager.clear()
        self.menu = None

    def new_game(self):
        self.clear_menu()
        self.menu = GameSetupMenu(self)

    def start_game(self, name: str):
        if len(name) <= 0 or name.isspace():
            self.game = Game(DEFAULT_PLAYER_NAME, self)
        else:
            self.game = Game(name, self)
        self.clear_menu()

    def load_game_menu(self):
        self.clear_menu()
        self.menu = LoadGameMenu(self)

    def load_game(self, filename):
        self.game = load_game(filename, self)
        self.clear_menu()

    def delete_game(self, filename):
        delete_game_file(filename)
        self.clear_menu()
        self.menu = LoadGameMenu(self)

    def back_to_main_menu(self):
        self.game = None
        self.clear_menu()
        self.menu = MainMenu(self)

    def open_finished_game_menu(self):
        self.menu = FinishedGameMenu(self)

    def quit(self):
        arcade.exit()
