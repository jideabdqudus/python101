from turtle import Screen, Turtle
from paddle import Paddle

screen = Screen()
paddle = Paddle()


screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("Ping Pong")


screen.listen()
screen.onkey(fun=paddle.move_paddle_up, key="Up")
screen.onkey(fun=paddle.move_paddle_down, key="Down")
screen.exitonclick()


# Create the screen
# Create and move a paddle
# Create another paddle
# Create a ball and move it
# Detect collision with wall and bounce
# Detect collision with paddle
# Detect when paddle misses
# Keep score
