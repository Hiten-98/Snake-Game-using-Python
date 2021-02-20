from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.goto(100,230)
        self.write(f"SCORE: {self.score}", align="left", font=("arial", 30, "bold"))


    def increment_score(self):
        self.score = self.score + 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(-60,-60)
        self.write("""
         ____________
        |                        |
        | Game Over  |
        |___________|""", align="center", font=("calibri", 40, "bold"))
