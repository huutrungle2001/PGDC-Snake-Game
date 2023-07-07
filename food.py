import random
from turtle import Turtle


class Food(Turtle):
    """
    This class is responsible for creating the food for the snake to eat.
    """

    def __init__(self, length=1, width=1):
        """
        The constructor for Food class.

        Args:
            length (int): The length of the food.
            width (int): The width of the food.
        """
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=length, stretch_wid=width)
        self.color("white")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        """
        Refreshes the food's position.
        """
        random_x = random.randint(-260, 260)
        random_y = random.randint(-260, 260)
        self.goto(random_x, random_y)
