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

def game_area():			# make the game area
	return

def game_area_changer():			# change the size of game area
	pass

def color_generator():				# generate random hexa color
	pass

def snake_body():					# draw the snake body, according to its movement
	return

def change_fov():					# change the field of view of player
	return

def change_game_speed():			# change the speed of the game
	return

def snake_sprint():				# sense if a key/ button is pressed to make snake sprint
	return

def snake_movement():			# bind the snake movement with keys
	return

def make_scoreboard():			# prints a scoreboard on the screen
	return

def timer():						# print a timer on the screen
	return

def make_minimap():					# print a minimap on the screen
	return

def boss_assigner():			# assign boss to a random player
	return

def respawn_generator():				# automatically generate a spawn location
	return


def collision_detection():				# detect collision with other players
	return

def food_generator():						# randomly generate food
	return

def food_collision():					# check if player's snake eat the food or not
	return

def server_holder():				# set up a server
	return

def stats():					# print some stats from the gameplay
	return


#######################################################################

### MAIN PROGRAM ######################################################
openingScreen()			# draw the opening screen
snake_movement()		# bind the snake movement with keys
game_area()				# make the game area
game_area_changer()		# change the size of game area
color_generator()		# generate random hexa color
snake_body()			# draw the snake body, according to its movement
change_fov()			# change the field of view of player
change_game_speed()		# change the speed of the game
snake_sprint()			# sense if a key/ button is pressed to make snake sprint
make_scoreboard()		# prints a scoreboard on the screen
timer()					# print a timer on the screen
make_minimap()			# print a minimap on the screen
boss_assigner()			# assign boss to a random player
respawn_generator()		# automatically generate a spawn location
collision_detection()	# detect collision with other players
food_generator()	 	# randomly generate food
food_collision()	 	# check if player's snake eat the food or not
server_holder()			# set up a server
stats()					# print some stats from the gameplay
loop()					# start the game loop
turtle.mainloop()		# keep window open until user closes it
#######################################################################
