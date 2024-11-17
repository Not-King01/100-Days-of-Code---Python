from turtle import Screen
from food import Food
from snake import Snake
from score_board import ScoreBoard
import time
screen = Screen()
screen.setup(600, 600)
screen.bgcolor('black')
screen.title("Snake Game")
screen.tracer(0)
snake = Snake()
food = Food()
scoreBoard = ScoreBoard()


user_interest = screen.textinput("Snake Game", "Welcome to my snake game!! Press 'y' to enter... ")
while user_interest == 'y':
    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.right, "Right")
    screen.onkey(snake.left, "Left")
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.turtles[0].distance(food) < 15:
        food.refresh()
        scoreBoard.increase_score()
        snake.increase()

    if snake.turtles[0].xcor() > 280 or snake.turtles[0].xcor() < -280 or snake.turtles[0].ycor() > 280 or snake.turtles[0].ycor() < -280 :
        scoreBoard.reset()
        snake.reset()
        scoreBoard.update_score_board()

    for turtle in snake.turtles[1:]:
        if snake.turtles[0].distance(turtle) < 10:
            scoreBoard.reset()
            snake.reset()
            scoreBoard.update_score_board()



screen.exitonclick()