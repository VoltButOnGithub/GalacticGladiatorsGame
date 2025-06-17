from GalacticGladiators.game_texts import DELETE
from GalacticGladiators.menu.styles.button_styles import RED_STYLE
from GalacticGladiators.menu.widgets.button import Button


class DeleteSaveButton(Button):
    def __init__(self, filename: str, app: 'Application'):
        self.filename = filename
        self.app = app
        super().__init__(text=DELETE, on_click=self.delete_game, width=100, style=RED_STYLE)

    def delete_game(self):
        self.app.delete_game(self.filename)
