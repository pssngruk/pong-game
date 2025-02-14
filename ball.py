from turtle import Turtle
import random

class Ball:
    def __init__(self):
        self.spawn_ball()

    def spawn_ball(self):
        self.ball = Turtle()
        self.ball.shape("circle")
        self.ball.penup()

    def bounce(self,paddle):
        paddle_angle = self.ball.towards(paddle)
        random_paddle_angle = random.randint(-20,20) + paddle_angle
        self.ball.goto()
