from turtle import Turtle

class TurtlePlayer(Turtle):
    def __init__(self):
        super().__init__()
        self.reset()


    def goUp(self):
        self.forward(10)

    def reset(self):
        self.shape("turtle")
        self.penup()
        self.setpos(0, -380)
        self.setheading(90)
