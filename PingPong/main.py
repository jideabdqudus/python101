from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("Ping Pong")
screen.tracer(0)

ball = Ball()
paddle = Paddle((350, 0))
second_paddle = Paddle((-350, 0))
left_score = 0
right_score = 0
scoreboard = Scoreboard()

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
    if ball.distance(paddle) < 50 and ball.xcor() > 330 or ball.distance(second_paddle) < 50 and ball.xcor() < -330:
        ball.bounce(1, -1)
    if ball.ycor() > 300 or ball.ycor() < -300:
        ball.bounce(-1, 1)
    if ball.xcor() > 390:
        scoreboard.l_point()
        ball.reset_position()
    if ball.xcor() < -390:
        right_score += 1
        scoreboard.r_point()
        ball.reset_position()

screen.exitonclick()
