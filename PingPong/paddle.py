from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, coordinates):
        super().__init__()
        self.coordinates = coordinates
        self.create_paddle(coordinates)

    def create_paddle(self, coordinates):
        self.shape("square")
        self.penup()
        self.color("white")
        self.goto(coordinates)
        self.turtlesize(stretch_wid=5, stretch_len=1)

    def move_paddle_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def move_paddle_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
