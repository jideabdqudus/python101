from turtle import Turtle, Screen, colormode
from random import choice, randint

kags = Turtle()
print(kags)
kags.shape("turtle")
kags.color("blue", "yellow")
kags.forward(100)
kags.right(90)
kags.forward(100)
kags.right(90)
kags.forward(100)
kags.right(90)
kags.forward(100)

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()

turtle = Turtle()
colormode(255)

colors = ["red", "SeaGreen", "wheat", "yellow", "black", "purple", "IndianRed", "DeepSkyBlue", "SlateGray"]
directions = [0, 90, 180, 270]

for _ in range(200):
    turtle.shape("turtle")
    turtle.width(10)
    turtle.speed("fast")
    random_int = randint(1, 255)
    random_int2 = randint(1, 255)
    random_int3 = randint(1, 255)
    tup = (random_int, random_int2, random_int3)
    turtle.pencolor(tup)
    # turtle.color(choice(colors))
    turtle.forward(30)
    turtle.setheading(choice(directions))


screen = Screen()
screen.exitonclick()


turtle = Turtle()



turtle.dot()

def draw_spirograph(size_of_spirograph):
    for _ in range(int(360 / size_of_spirograph)):
        random_int = randint(1, 255)
        random_int2 = randint(1, 255)
        random_int3 = randint(1, 255)
        tup = (random_int, random_int2, random_int3)
        turtle.speed("fastest")
        turtle.color(tup)
        turtle.circle(100)
        turtle.setheading(turtle.heading() + size_of_spirograph)

draw_spirograph(5)

screen = Screen()

screen.exitonclick()