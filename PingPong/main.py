from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("Ping Pong")
screen.tracer(0)

ball = Ball()
paddle = Paddle((350, 0))
second_paddle = Paddle((-350, 0))

screen.listen()
screen.onkey(fun=paddle.move_paddle_up, key="Up")
screen.onkey(fun=paddle.move_paddle_down, key="Down")
screen.onkey(fun=second_paddle.move_paddle_up, key="w")
screen.onkey(fun=second_paddle.move_paddle_down, key="s")


game_is_on = True
while game_is_on:
    time.sleep(0.01)
    screen.update()
    ball.move()
    if paddle.distance(ball) < 20:
        ball.bounce(-1)
    if ball.ycor() > 295 or ball.ycor() < -295:
        ball.bounce(-1)
    if ball.xcor() > 380 or ball.xcor() < -380:
        game_is_on = False
screen.exitonclick()

# Create the screen
# Create and move a paddle
# Create another paddle
# Create a ball and move it
# Detect collision with wall and bounce
# Detect collision with paddle
# Detect when paddle misses
# Keep score
