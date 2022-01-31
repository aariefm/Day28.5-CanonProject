from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.pu()
        self.ht()
        self.score = 0
        self.color("white")
        self.sety(250)
        self.write(f"Score: {self.score}", align="Center", font=("Courier", 16, "normal"))

    # def score(self):
    #     self.score += 1

    def update(self):
        self.clear()
        self.write(f"Score: {self.score}", align="Center", font=("Courier", 16, "normal"))



