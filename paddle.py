from turtle import Turtle


class Paddle:
    def __init__(self,player):
        self.make_paddle(player)


    def make_paddle(self,player):
        paddle = Turtle(shape = "square")
        paddle.penup()
        paddle.resizemode("user")
        paddle.shapesize(4,1)

        if player == "left":
            paddle.goto(-420,0)
            paddle.color("blue")
        else:
            paddle.goto(420,0)
            paddle.color("red")
