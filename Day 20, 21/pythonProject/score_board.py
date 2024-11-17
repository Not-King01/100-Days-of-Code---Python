from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 20, "bold")

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.f = open("data.txt", "r")
        self.highscore = int(self.f.read())
        self.f.close()
        self.hideturtle()
        self.color('white')
        self.penup()
        self.goto(0, 260)
        self.update_score_board()

    def update_score_board(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore}", False, ALIGNMENT, FONT )

    def increase_score(self):
        self.score += 1
        self.update_score_board()

    def reset(self):
        if self.score > int(self.highscore):
            self.highscore = self.score
            with open("data.txt", "w") as file:
                file.write(str(self.score))
        self.score = 0

