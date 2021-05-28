from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.score = 0
        self.penup()
        self.goto(0, 280)
        self.write(f"score :{self.score}", False, "center", font=("Courier", 10, "normal"))
        self.hideturtle()

    def add_score(self):
        self.score += 1
        self.clear()
        self.write(f"score :{self.score}", False, "center", font=("Courier", 10, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, "center", font=("Courier", 20, "normal"))
