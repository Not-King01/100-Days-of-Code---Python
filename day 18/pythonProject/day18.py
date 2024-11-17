import turtle
import random
from turtle import Screen

turtle.colormode(255)

t = turtle.Turtle()
turtle.Screen()
colors = [(126, 159, 28), (126, 128, 27), (75, 138, 244), (155, 206, 223), (63, 241, 5), (125, 231, 13), (20, 63, 57),
          (234, 152, 13), (241, 250, 43), (231, 14, 162), (222, 48, 45), (47, 127, 47), (28, 153, 132), (212, 177, 136),
          (198, 184, 117), (138, 13, 145), (123, 190, 58), (49, 117, 7), (161, 250, 171), (141, 105, 10),
          (178, 213, 154), (227, 235, 233), (143, 158, 2), (205, 251, 105), (144, 200, 103), (187, 123, 15),
          (30, 14, 249), (28, 10, 125), (112, 214, 215), (77, 42, 90)]
x = 0
y = 0
t.speed("fastest")

def print_10_dots():
    for i in range(10):
        t.color(random.choice(colors))
        t.begin_fill()
        t.dot(20)
        t.end_fill()
        t.pu()
        t.forward(40)
        t.pd()

for _ in range(10):
    t.setheading(225)
    t.pu()
    t.fd(300)
    t.pd()
    t.setheading(0)
    print_10_dots()
    y += 30
    t.pu()
    t.goto(0, y)
    t.pd()
Screen().exitonclick()