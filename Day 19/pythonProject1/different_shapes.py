from turtle import Turtle, Screen
import random

tim = Turtle()
screen = Screen()
number = 3

colors = ['red', 'blue', 'yellow', 'green', 'black']
screen.delay(0.5)

while number != 11:
    tim.color(random.choice(colors))
    for i in range(number):
        tim.fd(100)
        tim.left(360/number)
    number += 1

screen.exitonclick()