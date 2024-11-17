import turtle
import random
from turtle import Turtle, Screen
from turtledemo.paint import changecolor

is_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput("Your bet",
                            "Which color of the Turtle you bet on? ")
colors = ["red", "orange", "yellow", "green", "blue", "violet", "indigo"]
positions = [120, 80, 40, 0, -40, -80, -120]
turtles = []

for _ in range(0,7):
    t = Turtle(shape="turtle")
    t.color(colors[_])
    t.penup()
    t.goto(-230, positions[_])
    turtles.append(t)

if user_bet:
    is_on = True

while is_on:
    for turtle in turtles:
        random_dist = random.randint(0, 10)
        turtle.forward(random_dist)
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won. The {winning_color} Turtle is the winner!")
                is_on = False
            else:
                print(f"You lost. The {winning_color} Turtle is the winner!")
                is_on = False

screen.exitonclick()
