from turtle import Turtle


class Scoreboard(Turtle):
    """
    This class is responsible for keeping track of the score. It also displays
    the score and the high score.
    """

    # Class Attributes
    ALIGNMENT = "center"
    FONT = ("Monaco", 16, "normal")

    def __init__(self):
        """
        The constructor for Scoreboard class.
        """
        super().__init__()
        self.score = 0
        self.get_score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.file = open("score.txt", "r")
        self.get_score = self.file.read()
        self.file.close()
        self.write(
            f"Score: {self.score}   High Score: {int(self.get_score)}", align=Scoreboard.ALIGNMENT, font=Scoreboard.FONT)

    def increase_score(self, score=1):
        self.score += score
        self.clear()
        file = open("score.txt", "w")
        file.write(str(self.score))
        file.close()
        self.write(
            f"Score: {self.score} High Score: {int(self.get_score)}", align=Scoreboard.ALIGNMENT, font=Scoreboard.FONT)

    def reset(self):
        if self.score > int(self.get_score):
            self.get_score = self.score
        self.score = 0
        self.clear()
        self.write(
            f"Score: {self.score}   High Score: {self.get_score}", align=Scoreboard.ALIGNMENT, font=Scoreboard.FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER!", align=Scoreboard.ALIGNMENT,
                   font=Scoreboard.FONT)
