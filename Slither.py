import turtle
import math
import time
import random
import ctypes
from game import core

user32 = ctypes.windll.user32
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

playerList =  []
zoomMode = [1]
gameSpeeds = [1,1.5,2,4,8]

core(screensize, gameSpeeds)
turtle.mainloop()
