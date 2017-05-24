# stopIt.py
# Created by Dr. C, May 11, 2017

### MODULES ###
import turtle
import random
import math

### CONSTANTS ###
WSIZEX = 1000		# the screen window size in x-direction
WSIZEY = 750		# the screen window size in y-direction
WX	= 100			# the screen top left corner x coordinate
WY = 100			# the screen top left corner y coordinate
REFRESH = 25 		# the screen referesh time in milliseconds
PLAYERSIZE = 50		# size of player 
BGCOLOR = "black"	# background color
NTRAIL = 4			# number of stamps to keep each screen refresh
MAXV = 30			# starting speed of snake

### OBJECTS ###
player = turtle.Turtle()	# this creates the player object
screen = turtle.Screen()	# this creates the screen object
time = turtle.Turtle()		# this creates an object for writing the time to screen

### VARIABLES ###
theta = random.randint(0,360) 	# generates a random starting angle
vX = int(MAXV*math.cos(theta))  # x-velocity in pixels/refresh
vY = int(MAXV*math.sin(theta))	# y-velocity in pixels/refresh
minX = -2*PLAYERSIZE 	# left x-boundary
minY = -2*PLAYERSIZE 	# bottom y-bounday
maxX = 2*PLAYERSIZE 	# right x-bounday
maxY = 2*PLAYERSIZE 	# top y-boundary
counter = 0 			# keeps track of screen refreshes
tcounter = 0 			# keeps track of time (measured in refreshes)
startTimer = False 		# is True once tcounter starts counting

### BINDING FUNCTIONS ###
def up():				# this function gets called everytime user presses up arrow
	global vY 			# declare vY to be a global variable 
	global startTimer	# declare startTimer to be a global variable
	if not startTimer:	# if startTimer is not currently true
		startTimer = True 	# set startTimer to True
	vY = vY+1			# increase the y-velocity by 1 pixel/refresh

def down():				# this function gets called everytime user presses down arrow
	global vY 			# declare vY to be a global variable
	global startTimer 	# declare startTimer to be a global variable
	if not startTimer:	# if startTimer is not currently true
		startTimer = True 	# set startTimer to True
	vY = vY-1 			# decrease the y-velocity by 1 pixel/refresh

def right():			# this function gets called everytime user presses right arrow
	global vX 			# declare vX to be a global variable
	global startTimer 	# declare startTimer to be a global variable
	if not startTimer:  # if startTimer is not currently true
		startTimer = True 	# set startTimer to True
	vX = vX+1 			# increase the x-velocity by 1 pixel/refresh

def left():				# this function gets called everytime user presses left arrow
	global vX 			# declare vX to be a global variable
	global startTimer 	# declare startTimer to be a global variable
	if not startTimer:	# if startTimer is not currently true
		startTimer = True 	# set startTimer to True
	vX = vX-1 			# decrease the x-velocity by 1 pixel/refresh


### DO BINDING ###
screen.onkeypress(up,"Up")			# bind the up arrow to the function up
screen.onkeypress(down,"Down")		# bind the down arrow to the function down
screen.onkeypress(left,"Left")		# bind the left arrow to the function left
screen.onkeypress(right,"Right")	# bind the right arrow to the function right
screen.listen()						# make the screen 'listen' to user events

### FUNCTIONS ###
def drawPlayer():
	global player 				# declare player to be a global variable
	global counter				# declare counter to be a global variable
	global tcounter				# declare tcounter to be a global variable
	global time 				# declare time to be a global variable
	player.stamp()				# stamp the current location of the player
	if counter>NTRAIL:			# if the counter is bigger than constant NTRAIL
		player.clearstamps(1)	# clear the oldest stamp from screen	
	counter = counter+1			# increase the counter variable by 1
	if startTimer:				# if the timer has already started
		tcounter=tcounter+1		# increase the time counter by 1
	time.penup()				# lift up the time objects pen
	time.goto(-WSIZEX//2+50,WSIZEY//2-50) # goto the starting position for writing the time
	time.pendown()				# put the time objects pen down
	time.clear()				# clear the previous time from screen
	time.write("Time = "+str(tcounter),True,font=("Arial",20,"normal"))	# write time to screen

def openingScreen():						
	global player 						# declare player to be a global variable
	global screen 						# declare screen to be a global variable
	global time 						# declare time to be a global variable
	screen.setup(WSIZEX,WSIZEY,WX,WY)	# position and size the screen
	screen.bgcolor(BGCOLOR)				# set the background color of the screen
	screen.colormode(255)				# set the colormode to be rgb (0-255)
	screen.tracer(0,0)					# turn off animation
	player.ht()							# hide the player turtle
	player.penup()						# lift up the player's pen
	player.shape("circle")				# set the player shape to a circle
	player.shapesize(PLAYERSIZE//20)	# set the player size to PLAYERSIZE
	time.ht()							# hide the time object
	time.color("white")					# set the time objects color to white
	drawPlayer()						# call the function drawPlayer()
	screen.update()						# update the screen

def loop():
	global player 	# declare player to be a global variable
	global vX 		# declare vX to be a global variable
	global vY 		# declare vY to be a global variable
	global minX 	# declare minX to be a global variable
	global minY 	# declare minY to be a global variable
	global maxX 	# declare maxX to be a global variable
	global maxY 	# declare maxY to be a global variable

	if startTimer:		# if the timer has already started
		if minX>-WSIZEX//2+PLAYERSIZE: # if the left boundary is still too small
			minX=minX-1	# make the left x-boundary bigger
		if minY>-WSIZEY//2+PLAYERSIZE: # if the bottom boundary is still too small
			minY=minY-1	# make the bottom y-boundary bigger
		if maxX<WSIZEX//2-PLAYERSIZE: # if the right boundary is still too small
			maxX=maxX+1 # make the right x-boundary bigger
		if maxY<WSIZEY//2-PLAYERSIZE: # if the top boundary is still too small
			maxY=maxY+1 # make the top y-boundary bigger

	coords = player.pos() 	# current coordinates of player
	x = coords[0]			# current x-coordinate of player
	y = coords[1]			# current y-coordinate of player
	if x>=maxX or x<=minX:	# if player collides with left or right wall
		vX = -vX 			# reverse x-velocity (player bounces off wall)
	if y>=maxY or y<=minY:	# if player collides with top or bottom wall
		vY = -vY 			# reverse y-velocity (player bounces off wall)
	diffX = abs(x)/(WSIZEX//2)	# absolute difference of player x-position with centre
	diffY = abs(y)/(WSIZEY//2)  # absolute difference of player y-position with centre
	meanDiff = (diffX+diffY)/2 	# average difference of both directions
	x = x+vX 					# increment x-position by vX
	y = y+vY 					# increment y-position by vY
	player.color(int((1-diffX)*255),int((1-diffY)*255),int(meanDiff*255)) # set color of player
	player.goto(x,y) # move player to new position
	drawPlayer()	 # draw the player (call function drawPlayer())
	if vX==0 and vY==0:  # if player is stopped
		closingScreen()  # call closingScreen()
		return 			 # quit function 
	else:
		screen.ontimer(loop,REFRESH) 	# if player is still moving, call loop again after timer finishes

def closingScreen():
	global player 			# declare player as a global variable
	player.goto(-30,0)      # move player to (-30,0)
	player.write("YOU WIN!!!",True,font=("Arial",80,"normal")) # write YOU WIN on screen


### MAIN PROGRAM ###
openingScreen()			# draw the opening screen
loop()					# start the game loop 
turtle.mainloop()		# keep window open until user closes it