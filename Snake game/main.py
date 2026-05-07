from turtle import Screen , Turtle
import time
from snake import Snake
from Food import food
from Scoreboard import scoreboard
screen = Screen()
screen.bgcolor('Black')

screen.setup(600,600)
screen.title('My snake game')

screen.tracer(0)
snake=Snake()
food=food()
Scoreboard=scoreboard()

screen.listen()
screen.onkey(snake.up,'Up')
screen.onkey(snake.down,'Down')
screen.onkey(snake.left,'Left')
screen.onkey(snake.right,'Right')
game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.08)
    # Detect collisions with food
    if snake.head.distance(food) < 15:
        food.refresh()
        Scoreboard.increase_score()
        snake.extend()

    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor() >280 or snake.head.ycor() <-280:
        # Scoreboard.game_is_over()
        Scoreboard.reset_score()
        snake.reset()
        # game_is_on=False
    for segment in snake.segments :
        if segment == snake.head:## Excluding head of  snake --> it is for collision with snake itself
            pass
        elif snake.head.distance(segment)<10:
            Scoreboard.reset_score()
            snake.reset()


    # for segment in snake.segments[1:]: ## Excluding head of snake --> it is for collision with snake itself
    #     if snake.head.distance(segment)<10:
    #         # Scoreboard.game_is_over()
    #     #         Scoreboard.reset()
    #         # game_is_on = False

    snake.move()
screen.exitonclick()