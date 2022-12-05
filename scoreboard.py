from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.reset()
        self.round = 1
        self.write(f"Level: {self.round}", False, "center", ("Arial", 20, "bold"))

    def addScore(self):
        self.round +=1
        self.clear()
        self.write(f"Level: {self.round}", False, "center", ("Arial", 20, "bold"))

    def getScore(self):
        return self.round

    def gameOver(self):
        self.goto(0,0)
        self.write("Game Over", False, "center", ("Arial", 20, "bold"))

    def reset(self):
        self.ht()
        self.penup()
        self.goto(-350,360)