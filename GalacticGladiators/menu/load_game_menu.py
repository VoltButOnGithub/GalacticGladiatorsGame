import glob

from arcade.gui import UILabel, UIPadding

from GalacticGladiators.game_texts import CHOOSE_A_GAME_TO_LOAD, BACK_TO_MAIN_MENU, \
    NO_GAMES_TO_LOAD
from GalacticGladiators.menu.menu import Menu
from GalacticGladiators.menu.widgets.button import Button
from GalacticGladiators.menu.widgets.save_file import SaveFileBox
from GalacticGladiators.settings import SAVES_DIRECTORY


class LoadGameMenu(Menu):
    def __init__(self, app: 'Application'):
        game_saves = glob.glob(SAVES_DIRECTORY + '*.pk1')
        save_file_boxes = []
        for game_save in game_saves:
            save_file_boxes.append(SaveFileBox(game_save, app))
        widgets = [
            UIPadding((UILabel(text=CHOOSE_A_GAME_TO_LOAD, bold=True)), padding=[0, 0, 20, 0])
        ]
        if len(save_file_boxes) == 0:
            widgets.append(UIPadding(UILabel(text=NO_GAMES_TO_LOAD), padding=[0, 0, 20, 0]))
        for save_file_box in save_file_boxes:
            widgets.append(save_file_box)
        widgets.append(Button(text=BACK_TO_MAIN_MENU, on_click=app.back_to_main_menu))
        super().__init__(widgets)
