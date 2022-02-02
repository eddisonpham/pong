from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("purple")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.penup()
        self.X = 10
        self.Y = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.X
        new_y = self.ycor() + self.Y

        self.goto(new_x, new_y)

    def bounce_Y(self):
        self.Y *= -1

    def bounce_X(self):
        self.X *= -1
        self.move_speed *=0.9


    def reset_position(self):
        self.move_speed = 0.1
        self.goto((0, 0))
        self.bounce_Y()
        self.bounce_X()


