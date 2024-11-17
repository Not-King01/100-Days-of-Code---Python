import turtle as t
from turtle import Turtle, Screen
import random
t.colormode(255)

tim = Turtle()
screen = Screen()

def colors():
    r, g, b = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
    color = (r, g, b)
    return color

directions = [0, 90, 180, 270]
tim.width(10)

while True:
    tim.color(colors())
    tim.speed(20)
    tim.fd(20)
    tim.setheading(random.choice(directions))

