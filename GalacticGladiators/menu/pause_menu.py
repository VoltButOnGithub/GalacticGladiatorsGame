from GalacticGladiators.game_texts import QUIT, BACK_TO_MAIN_MENU, CONTINUE, TOGGLE_CHEATS
from GalacticGladiators.menu.menu import Menu
from GalacticGladiators.menu.widgets.button import Button


class PauseMenu(Menu):
    def __init__(self, app: 'Application'):
        buttons = [
            Button(text=CONTINUE, on_click=app.toggle_pause),
            Button(text=TOGGLE_CHEATS, on_click=app.game.toggle_cheats),
            Button(text=BACK_TO_MAIN_MENU, on_click=app.back_to_main_menu),
            Button(text=QUIT, on_click=app.quit),
        ]
        super().__init__(buttons)
