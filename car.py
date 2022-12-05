from turtle import Turtle
import turtle
import random

turtle.colormode(255)

class Car(Turtle):
    def __init__(self,speed):
        super().__init__()
        self.speed = speed
        self.penup()
        self.shape("square")
        self.shapesize(1,3)
        self.color(self.randomColor())
        self.setPosition()


    def setPosition(self):
        yCor = random.randint(-340,400)
        self.setpos(380,yCor)

    def move(self):
        self.backward(self.speed)

    def randomColor(self):
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        tup = (r, g, b)
        return tup

    def reset(self):
        self.ht()
        self.penup()