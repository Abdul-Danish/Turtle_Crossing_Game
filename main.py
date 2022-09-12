# Turtle_crossing_game (Day-23):

from turtle import Screen
from tim import Tim
from car import Car
from scoreboard import ScoreBoard
import time


screen = Screen()
screen.listen()
screen.tracer(0)
screen.setup(width=800, height=600)
cars_list = []
coordinates_list = [(-100, 170), (400, 120), (100, 70), (400, 70), (-200, 20), (-100, 20), (400, 20), (250, -30),
                    (-100, -30), (300, -80)]

tim = Tim()
scoreboard = ScoreBoard()

# car1 = Car(-100, 170)
# car2 = Car(400, 120)
# car3 = Car(100, 70)
# car03 = Car(400, 70)
# car4 = Car(-200, 20)
# car5 = Car(250, -30)
# car05 = Car(-100, -30)
# car6 = Car(300, -80)

for position in range(10):
    new_car = Car(coordinates_list[position])
    cars_list.append(new_car)

screen.onkey(tim.go_up, "Up")
# screen.onkey(tim.go_down, "Down")

alive = True
while alive:
    screen.update()
    time.sleep(scoreboard.move_speed)

    for position in range(10):

        # moving cars
        cars_list[position].move()

        # reset position of cars
        cars_list[position].reset()

        if tim.distance(cars_list[position]) < 20:
            alive = False
            scoreboard.game_over()

        if tim.ycor() > 200:
            scoreboard.increase_level()
            tim.level_up()
            scoreboard.increase_car_speed()


screen.exitonclick()