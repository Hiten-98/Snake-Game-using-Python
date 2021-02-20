from turtle import Turtle

class Design(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.boundary()
        self.author()

    def boundary(self):
        self.goto(0,230)
        self.write("_________________________________________", align="center", font=("arial", 30, "normal"))


    def author(self):
        self.goto(-205,235)
        self.write("Developed by: Coder and Maker", align="center", font=("calibri", 15, "italic"))
