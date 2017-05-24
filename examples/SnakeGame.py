import useful
from random import randint
import turtle

class snakeGame():

	def __init__(self,wSize,nGrid,gamespeeds,offsets,colors,path):
		self.wSize =  wSize# screen window size
		self.nGrid =  nGrid# number of grid spacings
		self.gamespeeds = gamespeeds# list of possible game speeds
		self.offLeft = 	offsets[0]	# left offset
		self.offRight = 	offsets[1]# right offset
		self.offBottom = 	offsets[2]# bottom offset
		self.offTop = 		offsets[3]# top offset
		self.bgColor = 		colors[0]# background color of screen
		self.padColor = 	colors[1]# color of padding
		self.gridColor = 	colors[2]# color of grid lines
		self.snakeColor = 	colors[3]# color of snake
		self.foodColor = 	colors[4]# color of food
		self.scoreColor = 	colors[5]# color of score text
		self.path = 		path# path to
		self.curScore = 0 	# keeps track of the player's score
		self.dirX = 0		# start the snake's x-direction as not moving
		self.dirY = 0		# start the snake's y-direction as not moving


	# def debug(self):
	# 	# you will change this method often. It is only for debugging.
	# 	# it is setup up currently to debug __init__
	# 	print(self.leftEdge)
	# 	print(self.rightEdge)
	# 	print(self.topEdge)
	# 	print(self.bottomEdge)
	# 	print(self.borderWid)
	# 	print(self.gridSize)
	# 	print(self.padding)
	# 	print(self.turtleSize)
	# 	print(self.startX)
	# 	print(self.startY)
	# 	print(self.endX)
	# 	print(self.endY)
	# 	print(self.snakePos)
	# 	print(self.foodPos)

	def choosePlayer(self):
		# parse data from high score file and store names and scores in lists
		[names,scores] = useful.parseHighScores(self.path)
		# print banner for user input section of game
		useful.banner(50,"*","Dr'C's Snake Game!")
		# loop until player chooses a valid name or makes a new name
		condition = True
		while True:
			print("\nChoose your player's number: ") # general prompt
			# prints all existing player names
			for i in range(len(names)//3):
				name = names[i*3]
				index = name.find("#")
				name = name[0:index]
				string = str(i)+": "+name
				print(string)
			# prints option to add a new player
			print(str(i+1)+": Add new player")
			# ask for user's player choice
			player = input("Enter your choice: ")
			# check if choice is valid
			if not player.isdigit() or int(player) not in range(0,len(names)+1):
				print("Not a valid player.. Please try again")
			# if valid, append new player to name and score list, and write a new score file
			elif int(player)==len(names)//3:
				newName = input("Please enter your name: ")
				names.append(newName+"#s#")
				scores.append("0")
				names.append(newName+"#m#")
				scores.append("0")
				names.append(newName+"#f#")
				scores.append("0")
				useful.writeHighScoreFile(self.path,names,scores)
				break
			else:
				break
		player = int(player) # convert player choice into integer
		# choose game difficulty
		while True:
			print("\nChoose game difficulty: ")
			print("0: Easy")
			print("1: Medium")
			print("2: Hard")
			difficulty = input("Enter your choice: ")
			if not difficulty.isdigit() or int(difficulty) not in range(3):
				print("Not a valid choice.. Please try again")
			else:
				difficulty = int(difficulty)
				break
		self.speed = self.gamespeeds[difficulty] # set the speed of the game
		# selects the index corresponding to a given player and difficulty
		self.player = 3*player+difficulty
		# extract player's name
		nameTemp = names[self.player]
		index = nameTemp.find("#")
		self.name = nameTemp[0:index]				# store player's name
		self.highScore = int(scores[self.player])	# store player's high score
		# self.debug() # uncomment this after you are done this method

	def gameParams(self):
		# the left-most boundary of the game board
		self.leftEdge = - self.wSize//2 + self.offLeft
		# the right-most boundary of the game board
		self.rightEdge = self.wSize//2 - self.offRight
		# the top-most boundary of the game board
		self.topEdge = self.wSize//2 - self.offTop
		# the bottom-most boundary of the game board
		self.bottomEdge  = - self.wSize//2 + self.offBottom
		# the width of the game board border
		self.borderWid = self.rightEdge-self.leftEdge
		# the width of a single grid square
		self.gridSize  = self.borderWid//self.nGrid
		# how much padding between outmost border and game grid
		self.padding   = self.borderWid%self.nGrid//2
		# the default size of a square turtle is 20.
		# turtleSize scales the snake and food so it fits in the grid
		self.turtleSize = self.gridSize/20
		# the starting value of x on the grid (left snake position)
		self.startX = -self.wSize//2 + self.offLeft + self.padding + self.gridSize/2
		# the starting value of y on the grid (bottom snake position)
		self.startY = -self.wSize//2 + self.offBottom + self.padding + self.gridSize/2
		# the ending value of x on the grid (right snake position)
		self.endX = self.wSize//2 - self.offRight - self.padding - self.gridSize/2
		# the ending value of y on the grid (top snake position)
		self.endY = self.wSize//2 - self.offTop - self.padding - self.gridSize/2
		# the starting position of the snake
		self.snakePos = [[self.startX,self.startY]]
		# the starting position of the food (will be overwritten later)
		self.foodPos = [0,0]
		# self.debug() # uncomment this after you are done this method

	def drawBoard(self):
		# create objects for game
		self.screen = turtle.Screen()	# screen object
		self.snake = turtle.Turtle()	# snake object
		self.food = turtle.Turtle()		# food object
		self.score = turtle.Turtle()	# score object

		# turn off animation
		self.screen.tracer(0,0)
		# setup the screen according to user setting
		self.screen.setup(self.wSize,self.wSize,0,0)
		# set the screen background color according to user setting
		self.screen.bgcolor(self.bgColor)
		# set the title of the screen (change this if you like)
		self.screen.title("Dr. C's Snake Game")

		# set up the snake properties
		self.snake.ht()	# hide the snake turtle
		self.snake.resizemode("user")	# set the resize mode of snake
		self.snake.turtlesize(self.turtleSize)	# resize the snake
		self.snake.shape("circle")				# set snake to square

		# make condensed variable names for geometric parameters
		left = self.leftEdge
		right = self.rightEdge
		top = self.topEdge
		bot = self.bottomEdge
		pad = self.padding

		# fill in the padding
		self.snake.color(self.padColor)
		self.snake.begin_fill()
		useful.drawRectangle(self.snake,left,right,top,bot)
		self.snake.end_fill()

		# make the grid background the same color as the screen background
		self.snake.color(self.bgColor)
		self.snake.begin_fill()
		useful.drawRectangle(self.snake,left+pad,right-pad,top-pad,bot+pad)
		self.snake.end_fill()

		# make the grid
		self.snake.color(self.gridColor)
		useful.makeSquareGrid(left+pad,bot+pad,self.gridSize,self.nGrid,self.snake)

		# position snake at its initial location
		self.snake.color(self.snakeColor)
		self.snake.penup()
		self.snake.goto(self.startX,self.startY)
		self.screen.update()
		self.snake.goto(self.startX,self.startY)
		self.snake.stamp()

		# position the food at its initial location
		self.food.ht()
		self.food.penup()
		self.food.shape("circle")
		self.food.resizemode("user")
		self.food.turtlesize(self.turtleSize)
		self.food.color(self.foodColor)
		self.newFoodPos()
		self.food.goto(self.foodPos[0],self.foodPos[1])
		self.food.stamp()

		# position the score object at its permanent location
		self.score.ht()
		self.score.penup()
		self.score.color(self.scoreColor)
		self.updateScore()	# initializes the score
		# # self.debug() # uncomment this after you are done this method

	def newFoodPos(self):
		# put intermediate variables here if you'd like
		position=[randint(0,50-1),randint(0,50-1)]
		self.foodPos[0] =self.leftEdge + self.padding + (position[0]+0.5) *self.gridSize
		self.foodPos[1] =self.bottomEdge + self.padding + (position[1]+0.5) * self.gridSize
		# self.debug() # uncomment this after you are done this method

	def updateScore(self):
		self.score.clear()
		self.score.goto(self.wSize//2-230,self.topEdge+15)
		if self.highScore<10:
			spaces="0000000"
		elif self.highScore<100:
			spaces="000000"
		elif self.highScore<1000:
			spaces="00000"
		elif self.highScore<10000:
			spaces="0000"
		elif self.highScore<100000:
			spaces="000"
		elif self.highScore<1000000:
			spaces = "00"
		elif self.highScore<10000000:
			spaces = "0"
		else:
			spaces=""
		self.score.write("High Score: "+spaces+str(self.highScore),False,"left",("Ariel",18,"bold"))
		self.score.goto(-self.wSize//2+10,self.topEdge+15)
		self.score.write("Score: "+str(self.curScore),False,"left",("Ariel",18,"bold"))
		# self.debug() # uncomment this after you are done this method

	def startGame(self):
		self.screen.onkeypress(self.up,"Up")
		self.screen.onkeypress(self.down,"Down")
		self.screen.onkeypress(self.right,"Right")
		self.screen.onkeypress(self.left,"Left")
		self.screen.listen()
		self.loop()

	def up(self):
		if self.dirY == -1:
			return
		else:
			self.dirY =1
			self.dirX =0
	# 	self.debug() # uncomment this after you are done this method

	def down(self):
		if self.dirY == 1:
			return
		else:
			self.dirY = -1
			self.dirX =0
		# self.debug() # uncomment this after you are done this method

	def left(self):
		if self.dirX == 1:
			return
		else:
			self.dirX = -1
			self.dirY =0
		# self.debug() # uncomment this after you are done this method

	def right(self):
		if self.dirX == -1:
			return
		else:
			self.dirX = 1
			self.dirY = 0
	# 	self.debug() # uncomment this after you are done this method

	def loop(self):
		quit = self.checkSelfCollision()
		# quit = False  # erase this line and uncomment the line above when ready
		if not quit:
			foodCollision = self.checkFoodCollision()
			self.updateSnakePos(foodCollision)
			self.updateScreen(foodCollision)
			self.screen.ontimer(self.loop,self.speed)
		else:
			self.gameOver()
		# self.debug() # uncomment this after you are done this method

	def checkFoodCollision(self):
		sx = self.snakePos[0][0]
		sy = self.snakePos[0][1]
		fx = self.foodPos[0]
		fy = self.foodPos[1]
		if sx==fx and sy==fy:
			self.newFoodPos()
			if self.curScore>=0 and self.curScore<1000:
				self.curScore = self.curScore+10
			elif self.curScore>=1000 and self.curScore<100000:
				self.curScore = self.curScore+1000
			else:
				self.curScore = self.curScore+100107

			if self.curScore>self.highScore:
			 	self.highScore = self.curScore
			self.updateScore()
			# self.debug() # uncomment this after you are done this method
			return True
		else:
			# self.debug() # uncomment this after you are done this method
			return False



	def updateSnakePos(self,doGrow):
		x = self.snakePos[0][0]		# current head position (x)
		y = self.snakePos[0][1]		# current head position (y)
		# change head x-pos to adjacent grid according to snake x-direction
		x += self.dirX*self.gridSize
		# change head y-pos to adjacent grid according to snake y-direction
		y += self.dirY*self.gridSize

		if x > self.rightEdge - self.padding or x < self.leftEdge + self.padding:
			if x > self.rightEdge - self.padding:
				x = self.leftEdge +  self.padding + 1/2*self.gridSize

			elif x < self.leftEdge + self.padding:
				x = self.rightEdge - self.padding - 1/2*self.gridSize

		if y > self.topEdge - self.padding or y < self.bottomEdge + self.padding:
			if y >	self.topEdge - self.padding:
				y = self.bottomEdge + self.padding + 1/2* self.gridSize

			elif y< self.bottomEdge + self.padding:
				y = self.topEdge - self.padding - 1/2 * self.gridSize

		# insert code that redefines x and y in the case that it hits the
		# border.  If the snake hits the border, it should appear on the
		# opposite border.
		## insert missing code here  ##


		##############################
		# insert the new head position into the snakePos list
		self.snakePos.insert(0,[x,y])
		# if the snake didn't collide with food, remove the tail
		if not doGrow:
			self.snakePos.pop(-1) # removes the oldest coordinate from list
		# self.debug() # uncomment this after you are done this method

	def updateScreen(self,doGrow):
		self.food.clearstamps(1)
		self.food.goto(self.foodPos)
		self.food.stamp()
		if not doGrow:
			self.snake.clearstamps(1)
		self.snake.goto(self.snakePos[0][0],self.snakePos[0][1])
		self.snake.stamp()
		self.screen.update()
		# self.debug() # uncomment this after you are done this method

	def checkSelfCollision(self):
		pos = self.snakePos[0]
		if pos in self.snakePos[1:]:
			# self.debug() # uncomment this after you are done this method
			return True
		else:
			# self.debug() # uncomment this after you are done this method
			return False

	def gameOver(self):
		self.updateScore()
		[names,scores] = useful.parseHighScores(self.path)
		scores[self.player] = str(self.highScore)
		useful.writeHighScoreFile(self.path,names,scores)
		self.score.goto(-100,self.topEdge+15)
		self.score.write("Game Over "+self.name+"!",False,"left",("Ariel",18,"bold"))
