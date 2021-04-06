from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import unittest


"""
def write_func(param):
    try:
        return int(param) + 5
    except ValueError as err:
        return err
    except TypeError as err:
        return err

class TestCase(unittest.TestCase):
    def setUp(self):
        print("About to run a function")
    def test_do_stuff(self):
        test_param = 10
        result = write_func(test_param)
        self.assertEqual(result, 15)

    def test_do_stuff2(self):
        test_param = "jajajs"
        result = write_func(test_param)
        self.assertIsInstance(result, ValueError)

    def test_do_stuff3(self):
        test_param = None
        result = write_func(test_param)
        self.assertIsInstance(result, TypeError)

    def test_do_stuff4(self):
        test_param = ' '
        result = write_func(test_param)
        self.assertIsInstance(result, ValueError)

   
if __name__ == '__main__':
    unittest.main()
"""

screen = Screen()
snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Xenzia")
screen.tracer(0)

screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect Collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect Collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()

    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()
