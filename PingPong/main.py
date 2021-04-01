from turtle import Screen
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
    if ball.distance(paddle) < 20 or ball.distance(second_paddle) < 20:
        ball.bounce(1, -1)
    if ball.ycor() > 300 or ball.ycor() < -300:
        ball.bounce(-1, 1)
    if ball.xcor() > 390 or ball.xcor() < -390:
        # paddle.write(f"GAME OVER", align="center", font=("Arial", 24, "normal"))
        game_is_on = False

screen.exitonclick()

# Detect collision with paddle
# Detect when paddle misses
# Keep score
