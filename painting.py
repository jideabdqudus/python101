#import colorgram
from turtle import Turtle, Screen, colormode
from random import choice

# rgb_colors = []
# colors = colorgram.extract('hirst.jpg', 30)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     rgb_colors.append(new_color)

rgb_colors = [(201, 164, 112), (239, 246, 241), (152, 75, 50),
              (221, 201, 138), (57, 95, 126), (170, 152, 44), (138, 31, 20), (135, 163, 183), (196, 94, 75), (49, 121, 88), (143, 177, 149), (95, 75, 77), (76, 39, 32), (164, 146, 157), (16, 98, 71), (232, 176, 165), (54, 46, 48), (32, 61, 76), (22, 83, 89), (182, 204, 176), (141, 22, 25), (86, 147, 127), (45, 66, 85), (8, 68, 53), (177, 94, 97), (222, 177, 182), (109, 128, 151)]

colormode(255)


turtle = Turtle()
turtle.hideturtle()
turtle.penup()
turtle.setheading(225)
turtle.forward(300)
turtle.setheading(0)
turtle.speed("fastest")


value = 10


for _ in range(value):
    for _ in range(value):
        turtle.dot(20, choice(rgb_colors))
        turtle.fd(50)
    turtle.left(90)
    turtle.fd(50)
    turtle.left(90)
    turtle.fd(500)
    turtle.setheading(360)

screen = Screen()
screen.window_width
screen.exitonclick()
