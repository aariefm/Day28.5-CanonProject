# Cannon Shooter Game project
from turtle import Screen
import time
from cannonball import Cannonball
from cannon import Cannon
from target import Target
from scoreboard import Scoreboard
from powerbutton import Powerbutton

# TODO 0: Create Screen Object with exitonclick
X_LOC = 0
Y_LOC = 0
screen = Screen()
screen.bgcolor("black")
screen.setup(1200, 600)
screen.title("Cannon Shooter")
screen.tracer(0)

# TODO 1: Create Cannon Object.

cannon = Cannon()
target = Target()
scoreboard = Scoreboard()
buttons = Powerbutton()

# TODO 2: Create Cannon Ball Object.
cannonball = Cannonball()
screen.update()

gameison = True

XYCOR = (0,0)

def click_location(x, y):
    xycor = (x, y)
    globals()["XYCOR"] = xycor
    return #xycor

# TODO 4: Create Event listener: Up and Down to adjust canon heading
screen.listen()
screen.onkeypress(key="Up", fun=cannon.tiltup)
screen.onkeypress(key="Down", fun=cannon.tiltdown)

while gameison:
    # TODO 5: Create Event listenener: Spacebar to launch cannon ball
    # TODO 3: Create Method for ball_launch.
    screen.onclick(click_location)

    buttonlevel = buttons.buttonpress(XYCOR[0], XYCOR[1])
    buttons.updatecolor(buttonlevel)

    screen.onkey(key="space", fun=cannonball.move)

    # Check power level:
    for index in range(0, 4):
        if buttons.buttons[index].color() == ("green", "green"):
            cannonball.power = 20 + 4*index

    # Check cannon launch
    if cannonball.fired:
        cannonball.move()
    if cannonball.distance(target) < 50:
        target.move_if_hit()
        scoreboard.score += 1
        scoreboard.update()

    cannonball.land(cannon)

    time.sleep(0.025)
    screen.update()

screen.mainloop()


# TODO 6: Create Method for ball lands: if ball on target score up, if ball not on target try again.