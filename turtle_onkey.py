from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()

def move_forward():
    turtle.forward(10)

def move_backward():
    turtle.backward(10)

def counter_clockwise():
    turtle.left(10)

def clockwise():
    turtle.right(10)

def clear_drawing():
    turtle.clear()
    turtle.penup()
    turtle.home()
    turtle.pendown()


screen.listen()
screen.onkey(fun=move_forward, key="w")
screen.onkey(fun=move_backward, key="s")
screen.onkey(fun=counter_clockwise, key="a")
screen.onkey(fun=clockwise, key="d")
screen.onkey(fun=clear_drawing, key="c")
screen.exitonclick()