from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.shapesize(0.5, 0.5)
        self.color("red")
        self.appear()

    def appear(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-205, 160)
        self.goto(random_x, random_y)

