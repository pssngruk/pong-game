from turtle import Turtle


class Paddle:
    def __init__(self):
        self.make_paddle()


    def make_paddle(self):
        paddle = Turtle(shape = "square")
        paddle.penup()
        paddle.resizemode("user")
        paddle.shapesize(4,1)
