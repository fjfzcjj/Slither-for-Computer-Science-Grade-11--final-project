import math
import turtle


def _onmove(self, item, fun, num=1, add=None):
    if fun is None:
        self.cv.unbind(item, 'Motion' % num)
    else:
        def eventfun(event):
            try:
                x, y = (self.cv.canvasx(event.x) / self.xscale,
                        -self.cv.canvasy(event.y) / self.yscale)
                fun(x, y)
            except Exception:
                pass

        self.cv.bind(item, 'Motion' % num, eventfun, add)


def onmove(self, fun, btn=1, add=None):
    self.screen._onmove(self.turtle._item, fun, btn, add)


turtle._tg_turtle_functions.append('onmove')
turtle.TurtleScreenBase._onmove = _onmove
turtle.RawTurtle.onmove = onmove


#
# def color_generator(self):
#     r = random.randint(0, 255)
#     generated = '#%02X%02X%02X' % (r(), r(), r())
#     return generated


class Core:
    def __init__(self, screensize, gamespeeds, gamepixelconstant=float(input('This Pixel CONSTANT will def how \
far each move is:'))):
        self.screensize = screensize
        self.gameSpeeds = gamespeeds
        self.gameAreaColor = '#000000'  # black
        self.slitherColor = '#00faff'  # aqua
        self.miniMapColor = '#ffffff'  # white
        self.mapEdgeColor = '#999999'  # gray
        self.edgeRed = '#ef0000'  # edgeRed
        self.currentScore = 0
        self.AreaCenter = [0, 0]  # will get changed when the slither moves around will mutiply this
        # in the future when calculating movement speed.
        self.PixelConstant = gamepixelconstant
        self.gameAreaDim = None
        self.gameAreaShape = None
        self.ontimerSpeed = None
        self.limiting_constant = None  # which defines how far each step of the slither is

        self.turning = None
        self.slitherChain = []
        self.food_sum = None
        self.max_length = None
        self.mouse = turtle.Turtle()
        self.screen = turtle.Screen()  # setup the screen and the drawing turtle
        self.area = turtle.Turtle()
        self.slither = turtle.Turtle()  # setup the slither

    def __str__(self):
        pass

    def gameareamaker(self, shape=input('Circle or square?\n'), dim=int(input('Dimension \
    (radius or side length ): \n'))):
        """This function draws the game area.
            Defined by user, the first input defines the shape of the game area,
            which is either a circle or a square.
            The second input defines the dimension of the game area, either the
            radius of the circle or the side length of the square.
        """

        self.gameAreaDim = dim  # sort arguments
        self.gameAreaShape = shape
        self.mouse.penup()
        self.mouse.shape('circle')
        self.mouse.color('white')
        self.mouse.turtlesize(0.2)
        self.mouse.st()
        self.slither.positions = [(0, 0)]
        self.screen.tracer(0, 0)
        self.screen.setup(self.screensize[0], self.screensize[1], 0, 0)
        self.screen.bgcolor(self.mapEdgeColor)
        self.screen.title = 'David\'s slither game'
        self.area.ht()

        if self.gameAreaShape in ['circle', 'Circle', 'C', 'c', 'cir', 'Cir', 'a really big big big circle', '1']:
            self.gameAreaShape = 'circle'
            self.area.penup()
            self.area.setposition(0, -self.gameAreaDim)
            self.area.pencolor(self.edgeRed)
            self.area.pensize(1)
            self.area.color(self.gameAreaColor)
            self.area.begin_fill()
            self.area.circle(self.gameAreaDim)  # draw a circle area with radius
            self.area.end_fill()

        else:
            self.gameAreaShape = 'square'
            self.area.penup()
            self.area.setposition(-1 / 2 * self.gameAreaDim,
                                  -1 / 2 * self.gameAreaDim)  # goes to the left bottom corner of
            #  the game area.
            self.area.setheading(0)
            self.area.pencolor(self.edgeRed)
            self.area.pensize(1)
            self.area.color(self.gameAreaColor)
            self.area.begin_fill()
            self.area.forward(self.gameAreaDim)
            self.area.setheading(90)
            self.area.forward(self.gameAreaDim)
            self.area.setheading(180)
            self.area.forward(self.gameAreaDim)  # draw a square with side length
            self.area.setheading(270)
            self.area.forward(self.gameAreaDim)
            self.area.end_fill()

    def update_game_area(self):
        new_x = self.AreaCenter[0]
        new_y = self.AreaCenter[1]

        self.area.clear()
        self.mouse.clear()
        if self.gameAreaShape == 'circle':
            self.area.setposition(new_x, new_y - self.gameAreaDim)
            # self.area.pencolor(self.edgeRed)
            # self.area.pensize(1)
            # self.area.color(self.gameAreaColor)
            self.area.begin_fill()
            self.area.circle(self.gameAreaDim)  # area a circle area with radius
            self.area.end_fill()

        else:
            self.area.setposition(new_x - 1 / 2 * self.gameAreaDim,
                                  new_y - 1 / 2 * self.gameAreaDim)  # goes to the left \
            # bottom corner of the game area.
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

    def lefton(self):
        self.turning = 'Left'

    def righton(self):
        self.turning = 'Right'

    def leftoff(self):
        self.turning = 'None'

    def rightoff(self):
        self.turning = 'None'

    def keyboard_movement(self):
        self.screen.onkeypress(self.righton, "Right")
        self.screen.onkeyrelease(self.rightoff, "Right")
        self.screen.onkeypress(self.lefton, "Left")
        self.screen.onkeyrelease(self.leftoff, "Left")
        self.screen.onscreenclick(self.mouse.goto)
        # self.mouse.onmove(self.mouse.goto)
        self.mouse.ondrag(self.mouse.goto)
        self.screen.listen()

    def slither_body(self):
        heading = self.slither.heading()
        radian_heading = math.radians(heading)
        move_distance = self.PixelConstant
        vector_x = math.cos(radian_heading) * move_distance
        vector_y = math.sin(radian_heading) * move_distance
        self.AreaCenter = [(self.AreaCenter[0] + vector_x), (self.AreaCenter[1] + vector_y)]
        self.update_game_area()

        # if len(self.slither.positions) < self.slither.max_length:
        #     pass
        #

    def game_speed_selector(self):
        print('Here are some game speed choices for you( above 16 will make your gamer > 60 FPS): \n')

        for i in range(len(self.gameSpeeds)):
            print(str(i + 1) + '. ' + str(self.gameSpeeds[i]), end='\n')

        x = int(input("Your choice is ( NUMBER! ): "))
        self.ontimerSpeed = int(800 / self.gameSpeeds[x - 1])  # will be in miliseconds

        print("Game speed set as: " + str(self.gameSpeeds[x - 1]) + " !")

    def changeheading(self):
        currentheading = self.slither.heading()
        if self.turning == 'None':
            return
        elif self.turning == 'Right':
            self.slither.setheading(currentheading - 3)
            return
        elif self.turning == 'Left':
            self.slither.setheading(currentheading + 3)
            return

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

    def slither_len_calculator(self, limiting_constant=int(input('Give me an liminting constant for the list: '))):
        pass

        food_eaten = self.food_sum
        self.limiting_constant = limiting_constant
        slither_len_limit = math.floor(self.limiting_constant * food_eaten)
        self.max_length = slither_len_limit
        return slither_len_limit

    def start_game(self):
        self.game_speed_selector()
        self.gameareamaker()
        # self.screen.degrees(360)

        self.keyboard_movement()

    def nothing(self):
        pass

    def game_loop(self):
        self.slither_body()
        self.changeheading()
        self.screen.ontimer(self.game_loop, self.ontimerSpeed)

        #
        # class slither():
        #     def __init__(self,name,screensize,zoomMode):
        #         self.name = name
        #         self.screensize = screensize
        #         self.zoomMode = zoomMode
        #
        #     def __str__(self):
        #         return "Name is: " + self.name + ". \n"  + "The screensize is: " + str(screensize[0]) +"px by " + \
        # str(screensize[1])+"px."
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