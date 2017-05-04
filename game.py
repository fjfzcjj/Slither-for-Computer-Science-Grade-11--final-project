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
        pass

    def gameAreaMaker(self, shape = input('Circle or square?\n'), dim = int(input('Dimension (radius or side length): \n')) ):
        """This function draws the game area.
Defined by user, the first input defines the shape of the game area,
which is either a circle or a square.
The second input defines the dimension of the game area, either the
radius of the circle or the side length of the square.
        """


        self.gameAreaShape = shape
        self.gameAreaDim = dim       # sort arguments


        self.screen = turtle.Screen()           # setup the screen and drawing turtle
        self.draw = turtle.Turtle()
        self.screen.tracer(0,0)
        self.screen.setup(self.screensize[0] , self.screensize[1] , 0 , 0 )
        self.screen.bgcolor(self.mapEdgeColor)
        self.screen.title = 'David\'s slither game'
        self.draw.ht()

        if self.gameAreaShape == 'circle':
            self.draw.penup()
            self.draw.setposition(0,-self.gameAreaDim)
            self.draw.pencolor(self.edgeRed)
            self.draw.pensize(1)
            self.draw.color(self.gameAreaColor)
            self.draw.begin_fill()
            self.draw.circle(self.gameAreaDim)              # draw a circle area with radius
            self.draw.end_fill()

        else:
            self.draw.penup()
            self.draw.setposition(-1/2*self.gameAreaDim, -1/2*self.gameAreaDim)     #goes to the left bottom corner of the game area.
            self.draw.setheading(0)
            self.draw.pencolor(self.edgeRed)
            self.draw.pensize(1)
            self.draw.color(self.gameAreaColor)
            self.draw.begin_fill()


            self.draw.forward(self.gameAreaDim)
            self.draw.setheading(90)
            self.draw.forward(self.gameAreaDim)
            self.draw.setheading(180)
            self.draw.forward(self.gameAreaDim)          # draw a circle area with radius
            self.draw.setheading(270)
            self.draw.forward(self.gameAreaDim)
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
        self.gameAreaMaker()





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
