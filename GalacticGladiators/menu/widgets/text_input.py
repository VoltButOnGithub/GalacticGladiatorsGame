import arcade
from arcade.gui import UIInputText, UIEvent, UITextEvent, UITextMotionEvent, UITextMotionSelectEvent


class TextInput(UIInputText):
    def __init__(self, width: int = 200, height: int = 30, max_length: int = 20):
        self.max_length = max_length
        super().__init__(width=width, height=height, text_color=arcade.color.WHITE)

    def on_event(self, event: UIEvent):
        if isinstance(event, UITextEvent):
            if (len(self.text) + len(event.text) < self.max_length) and event.text.isalnum():
                self.caret.on_text(event.text)
                self.trigger_full_render()
        elif isinstance(event, UITextMotionEvent):
            self.caret.on_text_motion(event.motion)
            self.trigger_full_render()
        elif isinstance(event, UITextMotionSelectEvent):
            self.caret.on_text_motion_select(event.selection)
            self.trigger_full_render()
