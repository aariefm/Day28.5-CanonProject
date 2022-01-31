from turtle import Turtle
import math
POWER = [5, 10, 15]

class Cannonball(Turtle):
    def __init__(self):
        super().__init__()
        self.pu()
        self.shape("circle")
        self.color("white")
        self.setx(-380)
        self.sety(-230)
        self.seth(45)
        self.fired = False
        self.grav = 9.81
        self.landed = True
        self.power = 30
        self.xspeed_0 = 0
        self.yspeed_0 = 0
        self.timer = 0

    def move(self):
        if self.timer == 0:
            self.xspeed_0 = self.power * math.cos(self.heading()*math.pi/180)
            self.yspeed_0 = self.power * math.sin(self.heading()*math.pi/180)
            print(self.xspeed_0)
            print(self.yspeed_0)
            self.timer += 2
            print(self.timer)
        self.fired = True
        # Governing Equation for projectile motion
        self.setx(self.xcor() + self.xspeed_0)
        self.sety((((self.yspeed_0 + self.grav * self.timer)-self.yspeed_0*self.yspeed_0)/(-2*self.grav)) + self.ycor())

        self.timer += 2
        # self.seth(self.heading() - self.grav)
        # self.forward(35)

    def land(self, cannon):
        if self.landed == True and self.fired == False:
            self.seth(cannon.heading())
            self.timer =0
            self.xspeed_0 = 0
            self.yspeed_0 = 0
        if self.ycor() <= -240:
            # self.landed = True
            self.fired = False
            self.landed = True
            self.forward(0)
            reset_pos = cannon.pos()
            self.goto(reset_pos)
            self.seth(cannon.heading())
            self.timer=0
            self.xspeed_0 = 0
            self.yspeed_0 = 0

