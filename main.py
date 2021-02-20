from turtle import  Screen
from snakebody import Snake
from food import Food
from scoreboard import Scoreboard
from design import Design
import time

screen = Screen()
screen.title("My Snake Game")
screen.bgcolor("Black")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()
design = Design()
design.boundary()
design.author()


screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on = True

while game_is_on:

    screen.update()
    time.sleep(0.1)
    #score.boundary()
    #score.author()
    snake.move()


    #detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increment_score()
        score.update_scoreboard()

    #detect collision with wall
    if snake.head.xcor() > 320 or snake.head.xcor() < -340 or snake.head.ycor() > 220 or snake.head.ycor() < -280:
        score.game_over()
        game_is_on = False

screen.exitonclick()