from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, x_pos, y_pos):
        self.x = x_pos
        self.y = y_pos
        super().__init__()
        self.color('white')
        self.shape('square')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto((self.x, self.y))

    def up(self):
        new_ycor =  self.ycor() + 20
        self.goto(self.x, new_ycor)

    def down(self):
        new_ycor = self.ycor() - 20
        self.goto(self.x, new_ycor)

