import random
from turtle import Turtle


class Food(Turtle):

    def __init__(self, length=1, width=1):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=length, stretch_wid=width)
        self.color("white")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-260, 260)
        random_y = random.randint(-260, 260)
        self.goto(random_x, random_y)
