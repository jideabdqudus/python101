from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super(Ball, self).__init__()
        self.create_ball()

    def create_ball(self):
        self.penup()
        self.shape("circle")
        self.color("white")
        self.turtlesize(stretch_wid=1, stretch_len=1)
        self.x_move = 1
        self.y_move = 1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce(self, variable_x, variable_y):
        self.y_move *= variable_x
        self.x_move *= variable_y