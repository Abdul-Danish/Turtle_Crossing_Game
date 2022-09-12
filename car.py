from turtle import Turtle
import random

COLOR_LIST = ["green", "yellow", "pink", "purple", "blue"]


class Car(Turtle):
    def __init__(self, x_y_coordinate):
        super().__init__()
        self.x_y_coordinate = x_y_coordinate
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=0.5, stretch_len=2)
        self.random_color()
        self.goto(x_y_coordinate)

    def move(self):
        self.setheading(180)
        self.forward(10)

    def reset(self):
        if self.xcor() < -390:
            self.goto(400, self.ycor())
            self.random_color()

    def random_color(self):
        self.color(random.choice(COLOR_LIST))


