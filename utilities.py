def konvertiere_sprite_sheet(sprite_sheet, x_num, y_num):
    frames = []

    for y in range(y_num):
        for x in range(x_num):
            frames.append(sprite_sheet.subsurface(x * 100, y * 100, 100, 100))
    return frames
