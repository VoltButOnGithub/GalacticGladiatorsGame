def draw_offset(sprite, offset):
    original_center_x = sprite.center_x
    original_center_y = sprite.center_y

    sprite.center_x += offset[0]
    sprite.center_y += offset[1]

    sprite.draw()

    sprite.center_x = original_center_x
    sprite.center_y = original_center_y
