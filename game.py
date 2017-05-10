import math, turtle, ctypes, random, timeit



class core():
    def __init__(self,screensize,gameSpeeds,gamePixelConstant = int(input('This Pixel CONSTANT will def how far each move is:'))):
        self.screensize = screensize
        self.gameSpeeds = gameSpeeds
        self.gameAreaColor = '#000000'   #black
        self.slitherColor = '#00faff'   #aqua
        self.miniMapColor = '#ffffff'   #white
        self.mapEdgeColor = '#999999'   #gray
        self.edgeRed = '#ef0000'        #edgeRed
        self.currentScore = 0
        self.AreaCenter = [0,0]                     # will get changed when the slither moves around
        self.PixelConstant = gamePixelConstant         # will mutiply this in
                                                        # the future when calculating movement speed.

    def __str__(self):
        pass

    def gameAreaMaker(self, shape = input('Circle or square?\n'), dim = int(input('Dimension (radius or side length): \n')) ):
        """This function draws the game area.
            Defined by user, the first input defines the shape of the game area,
            which is either a circle or a square.
            The second input defines the dimension of the game area, either the
            radius of the circle or the side length of the square.
        """



        self.gameAreaDim = dim       # sort arguments
        self.gameAreaShape = shape
        self.mouse = turtle.Turtle()
        self.mouse.penup()
        self.mouse.shape('circle')
        self.mouse.color('white')
        self.mouse.turtlesize(0.2)
        self.mouse.st()
        self.screen = turtle.Screen()           # setup the screen and the drawing turtle
        self.area = turtle.Turtle()
        self.slither = turtle.Turtle()           # setup the slither
        self.slither.positions = [(0,0)]
        self.screen.tracer(0,0)
        self.screen.setup(self.screensize[0] , self.screensize[1] , 0 , 0 )
        self.screen.bgcolor(self.mapEdgeColor)
        self.screen.title = 'David\'s slither game'
        self.area.ht()

        if self.gameAreaShape in ['circle','Circle','C','c','cir','Cir','a really big big big circle','1']:
            self.gameAreaShape = 'circle'
            self.area.penup()
            self.area.setposition(0,-self.gameAreaDim)
            self.area.pencolor(self.edgeRed)
            self.area.pensize(1)
            self.area.color(self.gameAreaColor)
            self.area.begin_fill()
            self.area.circle(self.gameAreaDim)              # draw a circle area with radius
            self.area.end_fill()

        else:
            self.gameAreaShape = 'square'
            self.area.penup()
            self.area.setposition(-1/2*self.gameAreaDim, -1/2*self.gameAreaDim)     #goes to the left bottom corner of the game area.
            self.area.setheading(0)
            self.area.pencolor(self.edgeRed)
            self.area.pensize(1)
            self.area.color(self.gameAreaColor)
            self.area.begin_fill()


            self.area.forward(self.gameAreaDim)
            self.area.setheading(90)
            self.area.forward(self.gameAreaDim)
            self.area.setheading(180)
            self.area.forward(self.gameAreaDim)          # draw a square with side length
            self.area.setheading(270)
            self.area.forward(self.gameAreaDim)
            self.area.end_fill()


    def updateGameArea(self):
        newX = self.AreaCenter[0]
        newY = self.AreaCenter[1]

        self.area.clear()
        self.mouse.clear()
        if self.gameAreaShape == 'circle':
                             #clear the areaing of 'area' first
            self.area.setposition(newX,newY - self.gameAreaDim)
            # self.area.pencolor(self.edgeRed)
            # self.area.pensize(1)
            # self.area.color(self.gameAreaColor)
            self.area.begin_fill()
            self.area.circle(self.gameAreaDim)              # area a circle area with radius
            self.area.end_fill()

        else:
           self.area.setposition(newX - 1/2*self.gameAreaDim, newY - 1/2*self.gameAreaDim)     #goes to the left bottom corner of the game area.
           self.area.setheading(0)
        #    self.area.pencolor(self.edgeRed)
        #    self.area.pensize(1)
        #    self.area.color(self.gameAreaColor)
           self.area.begin_fill()

           self.area.forward(self.gameAreaDim)
           self.area.setheading(90)
           self.area.forward(self.gameAreaDim)
           self.area.setheading(180)
           self.area.forward(self.gameAreaDim)
           self.area.setheading(270)
           self.area.forward(self.gameAreaDim)
           self.area.end_fill()
        self.screen.update()
    def leftOn(self):
        self.turning = 'Left'
        self.slither.setheading(self.slither.heading() + 2)

    def rightOn(self):
        self.turing = 'Right'
        self.slither.setheading(self.slither.heading() - 2)

    def leftOff(self):
        self.turning = None
        pass

    def rightOff(self):
        self.turning = None
        pass
    def keyboardMovement(self):
        self.screen.onkeypress(self.rightOn,"Right")
        self.screen.onkeyrelease(self.rightOff,"Right")
        self.screen.onkeyrelease(self.leftOff,"Left")
        self.screen.onkeypress(self.leftOn,"Left")
        self.screen.onscreenclick(self.mouse.goto)
        self.mouse.ondrag(self.mouse.goto)
        self.screen.listen()

    def slitherBody(self):
        hD = self.slither.heading()
        radianHD= math.radians(hD)
        moveDistance =  self.PixelConstant
        vectorX = math.cos(radianHD)* moveDistance
        vectorY = math.sin(radianHD)* moveDistance
        self.AreaCenter = [self.AreaCenter[0] + vectorX, self.AreaCenter[1] + vectorY]
        self.updateGameArea()

        # if len(self.slither.positions) < self.slither.maxLength:
        #     pass
        #

    def gameSpeedSelector(self):
        print('Here are some game speed choices for you( above 16 will make your gamer > 60 FPS): \n')

        for i in range(len(self.gameSpeeds)):
            print(str(i+1) + '. ' + str(self.gameSpeeds[i]), end = '\n')

        x = int(input("Your choice is ( NUMBER! ): "))
        self.ontimerSpeed = int(800 / self.gameSpeeds[x-1])
                          # will be in miliseconds

        print("Game speed set as: " + str(self.gameSpeeds[x-1]) + " !")

    def colorGenrerator(self):
        r = random.randint(0,255)
        generated = '#%02X%02X%02X' % (r(),r(),r())
        return generated


    def cursorSet(self):
        print(self.mouse.pos())
    # def zoomChanger(self):
    #     pass
    #
    # def foodGenerator(self):
    #     pass
    #
    #
    #
    # def coordinateToAngle(self):
    #     return angle
    #


    def slitherLengthCalculator(self, limitingConstant = int(input('Give me an liminting constant for the list: '))):
        pass

        foodEaten = self.slither.foodSum
        self.limitingConstant = limitingConstant
        posLenLimit = math.floor(self.limitingConstant * foodEaten)
        self.snake.maxLength = posLenLimit
        return posLenLimit

    def startGame(self):
        self.gameSpeedSelector()
        self.gameAreaMaker()
        # self.screen.degrees(360)

        self.keyboardMovement()

    def nothing(self):
        pass
    def gameLoop(self):
        self.slitherBody()
        self.cursorSet()
        self.screen.ontimer(self.gameLoop,self.ontimerSpeed)

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
