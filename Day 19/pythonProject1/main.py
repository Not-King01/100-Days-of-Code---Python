from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
tim.color("turquoise")
tim.shape("turtle")
# for i in range(4):
#     timmy_the_turtle.fd(100)
#     timmy_the_turtle.left(90)
user_choice = int(input("Enter no of dashed line: "))
for i in range(user_choice):
    tim.fd(20)
    tim.pu()
    tim.fd(20)
    tim.pd()



screen.exitonclick()