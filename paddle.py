from turtle import Turtle, Screen

class Paddle(Turtle):
    def __init__(self, position, up, down):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)
        self.screen.listen()
        self.screen.onkey(self.go_up, up)
        self.screen.onkey(self.go_down, down)


    def go_down(self):
        if self.ycor() >= -200:
            new_y = self.ycor() - 40
            self.goto(self.xcor(), new_y)
        else:
            pass

    def go_up(self):
        if self.ycor() <= 200:
            new_y = self.ycor() + 40
            self.goto(self.xcor(), new_y)
        else:
            pass

