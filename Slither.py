import turtle
import math
import time
import random
import ctypes
from game import core

user32 = ctypes.windll.user32                   # 1536*864
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)


zoomMode = [1]
gameSpeeds = [1,1.5,2,4,8,16,32,64,128,256,512,1024,2048,4096]


game = core(screensize, gameSpeeds)
game.startGame()
game.gameLoop()
turtle.mainloop()
