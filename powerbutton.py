from turtle import Turtle

class Powerbutton:

    def __init__(self):
        self.buttons = []
        for _ in range(1, 5):
            button = Turtle()
            button.color("white")
            button.pu()
            button.shape("circle")
            button.setx(-430)
            button.sety(-200 + _*45)
            button.write(f"     {_*20}%", False, "left", ("arial", 10, "normal"))
            self.buttons.append(button)

    def buttonpress(self, x, y):
        # print(" - - -- - - - - - - - - - - - -")
        # print(x)
        # print(y)
        if x > -440.0 and x < -420.0:
            for mult in range(1, 5):
                # print(mult)
                # print(float(-200 + mult*45 + 10))
                # print(float(-200 + mult*45 -10))
                if y < float(-200 + mult*45 + 10) and y > float(-200 + mult*45 -10):
                    buttonlevel = mult-1
                    #print(buttonlevel)
                    return buttonlevel
            return 0
        else:
            return 0


    def updatecolor(self, buttonlevel):
        for _ in range(0, 4):
            self.buttons[_].color("white")
        self.buttons[buttonlevel].color("green")