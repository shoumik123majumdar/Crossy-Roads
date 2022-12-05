from turtle import Screen
from car import Car
from turtle import Screen
from turtlePlayer import TurtlePlayer
from scoreboard import ScoreBoard
import random
import time

leader = open("TurtleCrosserLeaderboard.txt","a")

board = open("TurtleCrosserLeaderboard.txt","r")
scores = board.read().splitlines()
userNames = []
highScores = []
for score in scores:
    newList = score.split(":")
    userNames.append(newList[0])
    highScores.append(newList[1])


screen = Screen()
screen.setup(800,800)
screen.title("Turtle Crossing")

name = screen.textinput("Answer","Username:")
screen.tracer(0)
screen.listen()
turtwig = TurtlePlayer()
carsSpeed = 2

Cars = []

scoreboard = ScoreBoard()

def addCars():
    car = Car(carsSpeed)
    Cars.append(car)

def userStart(startTime):
    global refreshed
    if len(Cars) >= startTime:
        screen.onkey(turtwig.goUp, "Up")




addCars()
gameIsOn = True
counter = 1
endNum = 10
startTime = 1
refreshed = False

while gameIsOn:
    time.sleep(0.1)
    screen.update()
    if refreshed:
        screen.update()
    userStart(startTime)

    for car in Cars:
        car.move()
        if turtwig.distance(car)<27:
            scoreboard.gameOver()
            currentScore = scoreboard.getScore()
            for score in highScores:
                if currentScore>int(score):
                    highScores.insert(num,currentScore)
                    userNames.insert(num,name)
                else:
                    break
            for num in range(len(highScores)):
                leader.write(f"{userNames[num]}: Round{highScores[num]}")
            gameIsOn = False


    randNum = random.randint(0,endNum)
    if randNum == 0:
        addCars()

    if turtwig.ycor()>400:
        screen.reset()
        Cars.clear()
        turtwig.reset()
        scoreboard.reset()
        scoreboard.addScore()
        carsSpeed *= 1.25
        startTime+=2
        screen.onkey(turtwig.reset,"Up")
        endNum -= 1
        refreshed = False




leader.close()
board.close()
screen.exitonclick()
