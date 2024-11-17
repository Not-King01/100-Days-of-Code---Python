from turtle import Turtle
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.turtles = []
        self.create_turtles()

    def create_turtles(self):
        dist = 0
        for i in range(4):
            self.add_segment(dist)
            dist -= 20

    def add_segment(self, distance):
        t = Turtle()
        t.color('white')
        t.shape("square")
        t.pu()
        t.setx(distance)
        self.turtles.append(t)
    def add_new_segment(self, coordinates):
        t = Turtle()
        t.color('white')
        t.shape("square")
        t.pu()
        t.goto(coordinates)
        self.turtles.append(t)

    def move(self):
        for i in range(len(self.turtles)-1, 0, -1):
            new_xcor = self.turtles[i-1].xcor()
            new_ycor = self.turtles[i-1].ycor()
            self.turtles[i].goto(new_xcor, new_ycor)
        self.turtles[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.turtles[0].heading() != DOWN:
            self.turtles[0].setheading(UP)

    def down(self):
        if self.turtles[0].heading() != UP:
            self.turtles[0].setheading(DOWN)
    def right(self):
        if self.turtles[0].heading() != LEFT:
            self.turtles[0].setheading(RIGHT)
    def left(self):
        if self.turtles[0].heading() != RIGHT:
            self.turtles[0].setheading(LEFT)

    def increase(self):
        self.add_new_segment(self.turtles[-1].position())

    def reset(self):
        for turtle in self.turtles:
            turtle.goto(1000,1000)
        self.turtles.clear()
        self.create_turtles()

