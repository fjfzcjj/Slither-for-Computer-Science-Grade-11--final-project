import math, turtle, sys, ctypes, random, time


class core():
    def __init__(self,screensize,gameSpeeds):
        self.screensize = screensize
        self.gameSpeeds = gameSpeeds
        self.gameAreaColor = '#000000'   #black
        self.slitherColor = '#00faff'   #aqua
        self.miniMapColor = '#ffffff'   #white
        self.mapEdgeColor = '#999999'   #gray
        self.edgeRed = '#ef0000'        #edgeRed
        self.currentScore = 0

    def __str__(self):
        None

    def gameAreaMaker(self, radius = 500 , shape = 'circle'):
        self.gameAreaShape = shape
        self.gameAreaRadius = radius       # sort arguments


        self.screen = turtle.Screen()           # setup the screen and drawing turtle
        self.draw = turtle.Turtle()
        self.screen.tracer(0,0)
        self.screen.setup(self.screensize[0] , self.screensize[1] , 0 , 0 )
        self.screen.bgcolor(self.mapEdgeColor)
        self.screen.title = 'David\'s slither game'
        self.draw.ht()

        self.draw.penup()
        self.draw.setposition(0,0)
        self.draw.pencolor(self.edgeRed)
        self.draw.pensize(1)
        self.draw.color(self.gameAreaColor)
        self.draw.begin_fill()
        self.draw.circle(radius)              # draw a circle area with radius of 10000
        self.draw.end_fill()


    def colorGenrerator(self):
        r = random.randint(0,255)
        generated = '#%02X%02X%02X' % (r(),r(),r())
        return generated

    def zoomChanger(self):
        pass

    def foodGenerator(self):
        pass

    def gameLoop(self):
        gameAreaMaker()





#
# class slither():
#     def __init__(self,name,screensize,zoomMode):
#         self.name = name
#         self.screensize = screensize
#         self.zoomMode = zoomMode
#
#     def __str__(self):
#         return "Name is: " + self.name + ". \n"  + "The screensize is: " + str(screensize[0]) +"px by " + str(screensize[1])+"px."
#
#     def makePlayer(self):
#         playerList.append(self.name)
#         print(playerList)
#     def makeGameMenu(self):
#
#         turtle.bgcolor("#000000")
#         turtle.screensize(screensize[0],screensize[1])
#         turtle.title("Slither.David")
#         turtle.tracer(0,0)
#         # setup the screen according to user setting
#         turtle.setup(size[0],size[1],0,0)
#
# David = slither("David",screensize,zoomMode)
# David.makePlayer()
# turtle.mainloop
