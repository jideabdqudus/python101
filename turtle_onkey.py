from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()

def move_forward():
    turtle.forward(10)

def move_backward():
    turtle.backward(10)

def counter_clockwise():
    turtle.setheading(-360)

def clockwise():
    turtle.setheading(360)

def clear_drawing():
    screen.clear()
    turtle.home()


screen.listen()
screen.onkey(fun=move_forward, key="w")
screen.onkey(fun=move_backward, key="s")
screen.onkey(fun=counter_clockwise, key="a")
screen.onkey(fun=clockwise, key="d")
screen.onkey(fun=clear_drawing, key="c")
screen.exitonclick()