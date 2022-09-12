from turtle import Turtle


class Tim(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.goto(0, -110)
        self.setheading(90)

    def go_up(self):
        self.forward(25)

    # def go_down(self):
    #     self.backward(25)

    def level_up(self):
        self.goto(0, -110)
