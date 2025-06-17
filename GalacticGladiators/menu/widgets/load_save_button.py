from GalacticGladiators.menu.widgets.button import Button


class LoadSaveButton(Button):
    def __init__(self, filename: str, app: 'Application'):
        name = filename.split('\\')[-1]
        name = name.split('--')[0]
        self.filename = filename
        self.app = app
        super().__init__(text=name, on_click=self.load_game)

    def load_game(self):
        self.app.load_game(self.filename)
