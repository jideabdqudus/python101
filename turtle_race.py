from turtle import Turtle, Screen
from random import choice, randint

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_input = screen.textinput(title="Make a Bet", prompt="Which turtle would win the race? Pick a color: ")
colors = ["red", "orange", "green", "blue", "purple"]

horizontal_range = [100, 50, -50, -100, 0]

all_turtles = []

for color in colors:
    turtle = Turtle()
    all_turtles.append(turtle)
    turtle.shape("turtle")
    turtle.color(color)
    turtle.penup()
    rand_horizontal_range = choice(horizontal_range)
    horizontal_range.remove(rand_horizontal_range)
    turtle.goto(-230, rand_horizontal_range)


if user_input:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_input:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        rand_distance = randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()