from turtle import Turtle


class Scoreboard(Turtle):
    """
    This class is responsible for keeping track of the score. It also displays
    the score and the high score.

    Attributes:
        score (int): The current score.
        high_score (int): The high score.
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
        self.high_score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.file = open("score.txt", "r")
        self.high_score = self.file.read()
        self.file.close()
        self.write(
            f"Score: {self.score}   High Score: {int(self.high_score)}",
            align=Scoreboard.ALIGNMENT, font=Scoreboard.FONT)

    def increase_score(self, score=1):
        """
        Increases the score by the given amount.

        Args:
            score (int): The amount to increase the score by.
        """
        self.score += score
        self.clear()
        file = open("score.txt", "w")
        file.write(str(self.score))
        file.close()
        self.write(
            f"Score: {self.score} High Score: {int(self.high_score)}",
            align=Scoreboard.ALIGNMENT, font=Scoreboard.FONT)

    def reset(self):
        """
        Resets the score to 0.
        """
        if self.score > int(self.high_score):
            self.high_score = self.score
        self.score = 0
        self.clear()
        self.write(
            f"Score: {self.score}   High Score: {self.high_score}",
            align=Scoreboard.ALIGNMENT, font=Scoreboard.FONT)

    def game_over(self):
        """
        Displays the game over message.
        """
        self.goto(0, 0)
        self.write("GAME OVER!",
                   align=Scoreboard.ALIGNMENT,
                   font=Scoreboard.FONT)
