from turtle import Turtle
import random

class Target(Turtle):
    def __init__(self):
        super().__init__()
        self.pu()
        self.shape("square")
        self.color("white")
        self.move_if_hit()
        self.sety(-230)
        self.shapesize(3, 3)

    def move_if_hit(self):
        self.setx(random.randint(0, 550))