from GalacticGladiators.game_texts import QUIT, BACK_TO_MAIN_MENU
from GalacticGladiators.menu.menu import Menu
from GalacticGladiators.menu.widgets.button import Button


class FinishedGameMenu(Menu):
    def __init__(self, app: 'Application'):
        buttons = [
            Button(text=BACK_TO_MAIN_MENU, on_click=app.back_to_main_menu),
            Button(text=QUIT, on_click=app.quit),
        ]
        super().__init__(buttons, anchor_y='bottom', vertical=False)
