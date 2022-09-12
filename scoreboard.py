from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.level = 1
        self.move_speed = 0.1
        self.goto(-350, 250)
        self.write(arg=f"Level {self.level}", align="left", font=("Ariel", 15, "normal"))

    def increase_level(self):
        self.clear()
        self.level += 1
        self.write(arg=f"Level {self.level}", align="left", font=("Ariel", 15, "normal"))

    def increase_car_speed(self):
        self.move_speed *= 0.9

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="Game Over!", align="center", font=("Ariel", 30, "normal"))

