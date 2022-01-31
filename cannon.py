from turtle import Turtle


class Cannon(Turtle):
    def __init__(self):
        super().__init__()
        self.pu()
        # self.ht()
        self.shape("square")
        self.color("white")
        self.setx(-380)
        self.sety(-230)
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.seth(45)

        cannonbase = Turtle()
        cannonbase.shape("turtle")
        cannonbase.color("white")
        cannonbase.shapesize(stretch_wid=2, stretch_len=3)
        cannonbase.pu()
        cannonbase.setx(self.xcor()-15)
        cannonbase.sety(self.ycor()-15)
        cannonbase.seth(0)

    def tiltup(self):
        self.seth(self.heading() + 5)

    def tiltdown(self):
        self.seth(self.heading() - 5)