import turtle
from turtle import Turtle, Screen
import random
t = Turtle()
turtle.colormode(255)
t.speed("fastest")
screen = Screen()

def colors():
    r, g, b = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
    color = (r, g, b)
    return color

def spirograph(gap):
    for _ in range(360 // gap):
        t.color(colors())
        set_heading = t.heading() + gap
        t.setheading(set_heading)
        t.circle(100)

spirograph(10)

screen.exitonclick()