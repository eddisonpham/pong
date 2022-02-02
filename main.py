from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from score import Score
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((380, 0), "Up", "Down")
l_paddle = Paddle((-380, 0), "w", "s")
ball = Ball()
score = Score()


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce_Y()

    if ball.distance(r_paddle) <= 60 and ball.xcor() > 350:
        ball.bounce_X()

    if ball.distance(l_paddle) <= 60 and ball.xcor() < -350:
        ball.bounce_X()

    if ball.xcor() > 380:
        score.l_point()
        ball.reset_position()

    if ball.xcor() < -380:
        score.r_point()
        ball.reset_position()

screen.exitonclick()






screen.exitonclick()