# MODULES #
import turtle
import random
import math

# CONSTANTS #
CX = 0
CY = 0
SCALE = 2
KEEPGOING = True
NUMCIRCLES = 5
MAXR = 100
SCREENSIZE = 800

# functions #
def generateCircles(numCircles,maxR):
	xvals = list()
	yvals = list()
	rads = list()
	fillState = list()
	colors = list()
	minVal = -(SCREENSIZE//2-maxR)
	maxVal = SCREENSIZE//2-maxR
	for i in range(numCircles):
		num = random.random()
		rads.append(maxR*num)
		num = random.random()
		xvals.append(minVal+(maxVal-minVal)*num)
		num = random.random()
		yvals.append(minVal+(maxVal-minVal)*num)
		fillState.append(0)
		r = random.random()
		g = random.random()
		b = random.random()
		colors.append([r,g,b])
	return [xvals,yvals,rads,fillState,colors]

def drawMap(turtle,stretch,cornerX,cornerY,circles):
	xvals = circles[0]
	yvals = circles[1]
	rads = circles[2]
	turtle.clear()
	for i in range(len(xvals)):
		turtle.penup()
		turtle.goto(xvals[i]*stretch+cornerX,yvals[i]*stretch+cornerY)
		turtle.pendown()
		turtle.pencolor(circles[4][i][0],circles[4][i][1],circles[4][i][2])
		turtle.fillcolor(circles[4][i][0],circles[4][i][1],circles[4][i][2])
		if circles[3][i]:
			turtle.begin_fill()
		turtle.circle(rads[i]*stretch)
		if circles[3][i]:
			turtle.end_fill()
	screen.update()

def testFill(worker,turtle,circles,cornerX,cornerY,stretch):
	xvals = circles[0]
	yvals = circles[1]
	rads = circles[2]
	for i in range(len(circles[0])):
		diffX = xvals[i]*stretch+cornerX
		diffY = yvals[i]*stretch+cornerY+rads[i]*stretch
		diff = math.sqrt(diffX**2+diffY**2)
		if diff<20*stretch:
			circles[3][i] = 1
	return circles

def up ():
	global CY
	global bob
	CY = CY-10
	bob.setheading(90)
def down ():
	global CY
	CY = CY+10
	bob.setheading(270)

def right ():
	global CX
	CX = CX-10
	bob.setheading(0)

def left ():
	global CX
	CX = CX+10
	bob.setheading(180)

def quit ():
	global KEEPGOING
	KEEPGOING = False

def sUp():
	global SCALE
	SCALE = SCALE+0.25

def sDown():
	global SCALE
	SCALE = SCALE-0.25

def makeTurtles():
	bob = turtle.Turtle()
	worker = turtle.Turtle()
	worker.ht()
	screen = turtle.Screen()
	bob.goto(0,0)
	screen.tracer(0,0)
	screen.setup(SCREENSIZE,SCREENSIZE,0,0)
	screen.onkeypress(up,"Up")
	screen.onkeypress(down,"Down")
	screen.onkeypress(right,"Right")
	screen.onkeypress(left,"Left")
	screen.onkeypress(quit,"q")
	screen.onkeypress(sUp,"s")
	screen.onkeypress(sDown,"x")
	screen.listen()
	return [bob,worker,screen]

def playGame(keepGoing,bob,worker):
	global circles

	print(50*"*")
	print("CIRCLE FINDER!!!!")
	while keepGoing:
		summer = 0
		for i in range(len(circles[3])):
			summer = summer+circles[3][i]
		if summer == NUMCIRCLES:
			keepGoing = False
			print("YOU WIN!!!!")
			print(50*"*")
		drawMap(worker,SCALE,CX,CY,circles)
		circles = testFill(worker,bob,circles,CX,CY,SCALE)

### main program ###
circles = generateCircles(NUMCIRCLES,MAXR)
[bob,worker,screen] = makeTurtles()
playGame(KEEPGOING,bob,worker)
turtle.mainloop()