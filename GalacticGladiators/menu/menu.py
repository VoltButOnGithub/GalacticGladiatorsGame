from typing import List

import arcade
import arcade.gui
from arcade.gui import UIWidget


class Menu:
    def __init__(self, widgets: List[UIWidget], anchor_x='center', anchor_y='center', vertical=True):
        self.manager = arcade.gui.UIManager()
        self.manager.enable()
        self.widgets = arcade.gui.UIBoxLayout(spacing=100, vertical=vertical)
        for widget in widgets:
            self.widgets.add(widget)
        self.manager.add(arcade.gui.UIAnchorWidget(
            anchor_x=anchor_x,
            anchor_y=anchor_y,
            child=self.widgets
        ))
