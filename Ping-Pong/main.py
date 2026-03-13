import time
from turtle import Turtle , Screen
from paddle import paddle
from  Ball import ball
from scoreboard import Scoreboard

screen =Screen()
screen.bgcolor('black')
screen.setup(width=800 , height=600)
screen.title('Pong')
screen.tracer(0)

l_paddle = paddle((-350, 0))
r_paddle = paddle((350, 0))


screen.listen()
screen.onkey(r_paddle.go_up , 'Up')
screen.onkey(r_paddle.go_down , 'Down')

screen.onkey(l_paddle.go_up , 'w')
screen.onkey(l_paddle.go_down , 's')

ball=ball()
scoreboard=Scoreboard()


game_is_on = True

while game_is_on:
    screen.update()
    ball.move()
    time.sleep(0.05)
    if ball.ycor() >280 or ball.ycor() <-280: # Detect walls
        ball.bounce_y()
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 340) or (ball.distance(l_paddle) < 50 and ball.xcor() > -340): # Bounce on collision
        ball.bounce_x()

    if ball.xcor() > 380: # Reset on a miss
        ball.reset()
        scoreboard.r_points()
        scoreboard.update_scoreboard()

    if ball.xcor() <-380:
        ball.reset()
        scoreboard.l_points()
        scoreboard.update_scoreboard()


screen.exitonclick()