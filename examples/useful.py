## this is your first module
## put any functions you think you'll use time and again in here
## that way, you do the work once, and then benefit from it over and over again!

import math
def banner(wid,char,title):
	print(wid*char)
	print(" "*math.ceil((wid-len(title))/2)+title)
	print(wid*char)

def underline(wid):
	print("-"*wid)

def centreText(wid,text):
	print(" "*math.ceil((wid-len(text))/2)+text)

def parseHighScores(path):
	nameList = list()
	scoreList = list()
	highFile = open(path,"r")
	scoreData = highFile.readlines()
	highFile.close()
	setOfData = len(scoreData)
	for i in range(0,setOfData):
		splitterSpot=0
		theLine= scoreData[i]
		splitters=list()
		while True:
			if len(splitters)<2	:
				splitterSpot = theLine.find("#",splitterSpot)
				splitters.append(splitterSpot)
				splitterSpot = splitterSpot+1
			else:
				firstSplitter= splitters[0]
				secondSplitter= splitters[1]
				namePart= theLine[0:secondSplitter+1]
				scorePart= theLine[secondSplitter+1:]
				scoreNewLine = scorePart.find("\n")
				if	scoreNewLine != -1:
					scorePart = scorePart[0:-1]
				nameList.append(namePart)
				scoreList.append(scorePart)
				splitters=list()
				splitterSpot=0
				break
	return	[nameList,scoreList]

def writeHighScoreFile(path,names,scores):
	highFile = open(path,"w")
	for i in range(len(names)):
		highFile.write(names[i]+scores[i]+"\n")
	highFile.close()


def makeSquareGrid(left,bottom,step,ngrid,turtle):
	turtle.penup()
	for i in range(1,ngrid):
		turtle.penup()
		turtle.goto(left+i*step,bottom)
		turtle.pendown()
		turtle.goto(left+i*step,bottom+ngrid*step)

	for i in range(1,ngrid):
		turtle.penup()
		turtle.goto(left,bottom+i*step)
		turtle.pendown()
		turtle.goto(left+ngrid*step,bottom+i*step)	
	return

def drawRectangle(turtle,leftEdge,rightEdge,topEdge,bottomEdge):
	turtle.penup()
	turtle.goto(leftEdge,bottomEdge)
	turtle.pendown()
	turtle.goto(rightEdge,bottomEdge)
	turtle.goto(rightEdge,topEdge)
	turtle.goto(leftEdge,topEdge)
	turtle.goto(leftEdge,bottomEdge)
	return
