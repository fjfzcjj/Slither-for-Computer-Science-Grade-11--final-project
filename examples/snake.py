from SnakeGame import snakeGame
import turtle

# path to the high score file (change to a directory on your computer)
path = "/Users/David/snake/snakeHighScore.txt"

###### GAME SETTINGS  ################################
# the screen size the game will be played on: MUST BE A MULTIPLE OF 20
wSize = 804
# how many times to divide the game board to make a grid: MUST BE A POSITIVE INTEGER VALUE
nGrid = 50
# game refresh speed in milliseconds: MUST BE A POSITIVE NUMBER
gameSpeeds =[100,50,25] # speed order is SLOW, MED, FAST
# game board parameters:
# make sure offLeft+offRight == offBottom + offTop
offLeft = 30
offRight = 30
offBottom = 20
offTop = 40
offsets = [offLeft,offRight,offBottom,offTop]
# game colors
bgColor = "black"
padColor = "white"
gridColor = "blue"
snakeColor = "red"
foodColor = "green"
scoreColor = "white"
colors = [bgColor,padColor,gridColor,snakeColor,foodColor,scoreColor]
#############################################


game = snakeGame(wSize,nGrid,gameSpeeds,offsets,colors,path)  # the object that controls the snake game
# uncomment the following methods one at a time

game.choosePlayer() # user chooses an existing player or makes a new one and chooses game difficulty
game.gameParams() 	# calculates the necessary parameters for the game
game.drawBoard()	# creates game objects and draws the game board in starting configuration
game.startGame() 	# starts the game and quits when player loses

turtle.mainloop()  # don't uncomment this until you uncomment game.drawBoard()
