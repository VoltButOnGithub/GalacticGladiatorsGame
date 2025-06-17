from GalacticGladiators.game_texts import NEW_GAME, LOAD_GAME, QUIT
from GalacticGladiators.menu.menu import Menu
from GalacticGladiators.menu.styles.button_styles import RED_STYLE, ORANGE_STYLE, YELLOW_STYLE
from GalacticGladiators.menu.widgets.button import Button


class MainMenu(Menu):
    def __init__(self, app: 'Application'):
        buttons = [
            Button(text=NEW_GAME, on_click=app.new_game, style=RED_STYLE),
            Button(text=LOAD_GAME, on_click=app.load_game_menu, style=ORANGE_STYLE),
            Button(text=QUIT, on_click=app.quit, style=YELLOW_STYLE),
        ]
        super().__init__(buttons)
