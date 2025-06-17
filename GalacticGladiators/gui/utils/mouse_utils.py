import arcade


def set_cursor_hand() -> None:
    arcade.get_window().set_mouse_cursor(
        cursor=arcade.get_window().get_system_mouse_cursor(name=arcade.Window.CURSOR_HAND))


def set_cursor_default() -> None:
    arcade.get_window().set_mouse_cursor(
        cursor=arcade.get_window().get_system_mouse_cursor(name=arcade.Window.CURSOR_DEFAULT))
