from turtle import Turtle


class Snake:
    # Class attributes
    STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
    MOVE_DISTANCE = 20
    UP = 90
    DOWN = 270
    LEFT = 180
    RIGHT = 0
    """
    This class represents the snake in the game. The direction of the snake is 
    the direction of the head.

    Attributes:
        body: a list of turtle objects.
        head: the first turtle object in the body list.
    """

    def __init__(self):
        """
        The constructor for Snake class.
        """
        self.body = []
        self.create_snake()
        self.head = self.body[0]

    def create_snake(self):
        """
        This method creates the body of the snake by adding 3 turtle objects 
        to the body list.
        """
        for position in Snake.STARTING_POSITIONS:
            self.add_segment(position)

    def move(self):
        """
        This method moves the snake forward by 20 pixels.
        """
        for turtle_num in range(len(self.body) - 1, 0, -1):
            new_x = self.body[turtle_num-1].xcor()
            new_y = self.body[turtle_num-1].ycor()
            self.body[turtle_num].goto(new_x, new_y)
        self.body[0].forward(Snake.MOVE_DISTANCE)

    def add_segment(self, position):
        """
        This method adds a new segment to the snake.

        Args:
            position: a tuple of x and y coordinates.
        """
        turtle = Turtle(shape="square")
        turtle.penup()
        turtle.color("white")
        turtle.goto(position)
        self.body.append(turtle)

    def reset(self):
        """
        This method resets the snake to its original state.
        """
        for seg in self.body:
            seg.goto(1000, 1000)
        self.body.clear()
        self.create_snake()
        self.head = self.body[0]

    def extend(self):
        """
        This method adds a new segment to the snake.
        """
        self.add_segment(self.body[-1].position())

    def up(self):
        """
        This method changes the direction of the snake to up. The snake cannot
        move up if it is moving down.
        """
        if self.body[0].heading() != Snake.DOWN:
            self.body[0].setheading(Snake.UP)

    def down(self):
        """
        This method changes the direction of the snake to down. The snake cannot
        move down if it is moving up.
        """
        if self.body[0].heading() != Snake.UP:
            self.body[0].setheading(Snake.DOWN)

    def left(self):
        """
        This method changes the direction of the snake to left. The snake cannot
        move left if it is moving right.
        """
        if self.body[0].heading() != Snake.RIGHT:
            self.body[0].setheading(Snake.LEFT)

    def right(self):
        """
        This method changes the direction of the snake to right. The snake cannot
        move right if it is moving left.
        """
        if self.body[0].heading() != Snake.LEFT:
            self.body[0].setheading(Snake.RIGHT)
