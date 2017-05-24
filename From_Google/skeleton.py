# skeleton version of jump.py
# Created by Dr. C, May 20, 2017

### MODULES ###########################################################
import turtle
import random
import math
#######################################################################

### CONSTANTS #########################################################
# WINDOW PROPERTIES
WSIZEX = 700		# the screen window size in x-direction
WSIZEY = 820		# the screen window size in y-direction
WX = 0				# the screen top left corner x coordinate
WY = 0				# the screen top left corner y coordinate
REFRESH = 1 		# the screen refresh time in milliseconds
# PROGRAMMER CONSTANTS
DOPRINT = True     # PRINT INFO TO SCREEN WHEN TRUE
#######################################################################

### OBJECTS ###########################################################
player = turtle.Turtle()	# this creates the player object
screen = turtle.Screen()	# this creates the screen object
#######################################################################

### VARIABLES #########################################################
doLoop = True 	# this controls whether the program does another loop
counter = 0		# this counts how many screen refreshes have passed
#######################################################################

### BINDING FUNCTIONS #################################################
def quit():			# this function gets called when user presses Q
	global doLoop
	doLoop = False	# this will break the loop() function
	return
#########################################################################

### DO BINDING ##########################################################
screen.onkeypress(quit,"q")	# bind the q button to the function quit()
screen.listen()				# make the screen 'listen' to user events
#########################################################################

### FUNCTIONS ###########################################################
def drawPlayer():		# this function draws the current player
	global player
	# get the current coordinates of the player
	coords = player.pos()
	x = coords[0]
	y = coords[1]
	# update the player on the screen
	player.goto(x,y)
	player.clear()
	player.stamp()
	# return back to main program
	return

def openingScreen():  # this function opens screen and sets it up
	global screen
	global worker
	global player
	# set the initial screen properties
	screen.setup(WSIZEX,WSIZEY,WX,WY)
	screen.tracer(0,0)
	screen.bgcolor("black")
	# set the initial player properties
	player.color("orange")
	player.shape("circle")
	player.ht()
	player.stamp()
	#update the screen
	screen.update()
	#return back to main program
	return

def loop():		# this is the game's main loop function
	global doLoop
	global REFRESH
	global counter

	# when debugging, print to terminal
	if DOPRINT:
		print("Refresh #"+str(counter)) # print the current refresh
	counter = counter+1 # update refresh counter

	drawPlayer() # draw the player according to algorithm in drawPlayer()

	if doLoop:
		screen.ontimer(loop,REFRESH)  # if player hasn't quit yet, loop
	else:
		closingScreen()  	# player has quit
		return


def closingScreen():  # this is what happens when the player quits
	global screen
	print("THANKS FOR PLAYING!")
	screen.bye()
	return

def quantumTeleport(): # this is what happens if the player is much too small
	return
#######################################################################

### MAIN PROGRAM ######################################################
openingScreen()			# draw the opening screen
loop()					# start the game loop
turtle.mainloop()		# keep window open until user closes it
#######################################################################
