from turtle import Turtle
import time

class BallControl(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.sleep_time = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
        time.sleep(self.sleep_time)

    def border_control(self):
        if self.ycor() < -280 or self.ycor() > 280:
            self.y_move *= -1

    def increase_speed(self):
        self.sleep_time *= 0.9

