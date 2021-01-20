from turtle import Turtle


class Tags(Turtle):
    def __init__(self, input, x, y):
        super().__init__()
        self.hideturtle()
        self.color("blue")
        self.penup()
        self.goto(x, y)
        self.speed("fastest")
        self.write(input, align="center", font=("Arial", 8, "normal"))
