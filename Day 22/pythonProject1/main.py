from turtle import Screen, Turtle
from ball_control import BallControl
from paddle_control import Paddle
from score_board import Scoreboard

screen = Screen()
screen.title("Pong Game")
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.tracer(0)

ball = BallControl()
paddle1 = Paddle(350, 0)
paddle2 = Paddle(-350, 0)

score = Scoreboard()

screen.listen()
screen.onkey(paddle2.up, 'q')
screen.onkey(paddle2.down, 'a')
screen.onkey(paddle1.up, 'Up')
screen.onkey(paddle1.down, 'Down')

def collision(p1, p2, b):
    if ball.distance(paddle1) < 35 and ball.xcor() > 330 or ball.distance(paddle2) < 35 and ball.xcor() < -330:
        ball.x_move *= -1
        ball.increase_speed()

def game_over():
    if ball.xcor() >= 380:
        score.clear()
        score.l_point()
        ball.goto(0,0)
        ball.x_move *= -1
    if ball.xcor() <= -380:
        score.clear()
        score.r_point()
        ball.goto(0, 0)
        ball.x_move *= -1

while True:
    screen.update()

    score.update_score()
    ball.border_control()
    game_over()
    collision(paddle1, paddle2, ball)
    ball.move()






screen.exitonclick()