import arcade.gui
from arcade.gui import UILabel

from GalacticGladiators.game_texts import BACK_TO_MAIN_MENU, START_GAME, TYPE_A_NAME
from GalacticGladiators.menu.menu import Menu
from GalacticGladiators.menu.styles.button_styles import GREEN_STYLE
from GalacticGladiators.menu.widgets.button import Button
from GalacticGladiators.menu.widgets.text_input import TextInput


class GameSetupMenu(Menu):
    def __init__(self, app: 'Application'):
        self.app = app
        self.text_input = TextInput()
        self.text_input_padding = arcade.gui.UIPadding(child=self.text_input, padding=(5, 20, 5, 20))
        self.text_input_box = arcade.gui.UIBorder(child=self.text_input_padding,
                                                  border_width=5,
                                                  border_color=arcade.color.YELLOW)
        widgets = [
            UILabel(text=TYPE_A_NAME, bold=True),
            self.text_input_box,
            Button(text=START_GAME, on_click=self.start_game, style=GREEN_STYLE),
            Button(text=BACK_TO_MAIN_MENU, on_click=app.back_to_main_menu),
        ]
        super().__init__(widgets)

    def start_game(self):
        self.app.start_game(self.text_input.text)
