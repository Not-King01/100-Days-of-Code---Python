from turtle import Turtle, Screen
t = Turtle()
screen = Screen()

#functions

def move_forward():
    t.forward(10)

def move_backward():
    t.backward(10)

def clear():
    t.clear()
    t.penup()
    t.home()
    t.pendown()

def clockwise():
    t.setheading(t.heading() - 10)

def anti_clockwise():
    t.setheading(t.heading() + 10)


screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(clockwise, "d")
screen.onkey(anti_clockwise, "a")
screen.onkey(clear, "c")
screen.exitonclick()