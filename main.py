from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball


# Set up the screen

screen = Screen()
screen.setup(width = 900, height = 600)

# Set up the game

player = Paddle("left")
computer = Paddle("right")
ball = Ball()
screen.exitonclick()

game_running = True

while game_running:
    ball.start()
