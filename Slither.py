import turtle
import ctypes
import random
from game import Core

# CONSTANTS
user32 = ctypes.windll.user32                   # 1536*864
ScreenSize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)


zoomMode = [1]
GameSpeeds = [1, 1.5, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]


def color_generator():
    r = random.randint(0, 255)
    generated = '#%02X%02X%02X' % (r(), r(), r())
    return generated
# defined a color generator, returns a hexadecimal color
# %02X in C means hexadecimal code, but at least two digits(put 0 in front if needed.)
# Also, 255 = FF

game = Core(ScreenSize, GameSpeeds)
game.start_game()
game.game_loop()
turtle.mainloop()
