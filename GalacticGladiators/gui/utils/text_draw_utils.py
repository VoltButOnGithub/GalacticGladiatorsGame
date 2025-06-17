import arcade.color
from arcade import draw_text as arcade_draw_text


def draw_text(text, offset):
    arcade_draw_text(start_x=offset[0], start_y=offset[1], color=arcade.color.WHITE, text=text)


def draw_small_text(text, offset, width):
    arcade_draw_text(start_x=offset[0], start_y=offset[1], color=arcade.color.WHITE, text=text, font_size=10,
                     multiline=True, width=width)
