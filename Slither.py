import turtle
import ctypes
from game import Core

# CONSTANTS
user32 = ctypes.windll.user32                   # 1536*864
ScreenSize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)


zoomMode = [1]
GameSpeeds = [1, 1.5, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]


game = Core(ScreenSize, GameSpeeds)
game.start_game()
game.game_loop()
turtle.mainloop()
