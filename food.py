import random
from turtle import Turtle


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        ran_x = random.randint(-200, 200)
        ran_y = random.randint(-200, 200)
        self.goto(ran_x, ran_y)

    def refresh(self):
        ran1_x = random.randint(-200, 200)
        ran1_y = random.randint(-200, 200)
        self.goto(ran1_x, ran1_y)
