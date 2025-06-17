from typing import Callable

import arcade.gui
from arcade.gui import UIFlatButton

from GalacticGladiators.menu.styles.button_styles import DEFAULT_STYLE


class Button(UIFlatButton):
    def __init__(self, text: str, on_click: Callable, width: int = 200, height: int = 100, style: dict = DEFAULT_STYLE):
        super().__init__(text=text, width=width, height=height, style=style)
        self.on_click_event = on_click

    def on_click(self, event: arcade.gui.UIOnClickEvent):
        self.on_click_event()
