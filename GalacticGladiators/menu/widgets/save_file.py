from arcade.gui import UIBoxLayout

from GalacticGladiators.menu.widgets.delete_save_button import DeleteSaveButton
from GalacticGladiators.menu.widgets.load_save_button import LoadSaveButton


class SaveFileBox(UIBoxLayout):
    def __init__(self, filename: str, app: 'Application'):
        super().__init__(vertical=False)
        self.add(LoadSaveButton(filename, app))
        self.add(DeleteSaveButton(filename, app))
