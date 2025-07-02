from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scores
import time

SNAKE = Snake()
FOOD = Food()
SCORE = Scores()

screen = Screen()
screen.setup(width= 600, height= 600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

screen.listen()
screen.onkey(SNAKE.up, "Up")
screen.onkey(SNAKE.down, "Down")
screen.onkey(SNAKE.left, "Left")
screen.onkey(SNAKE.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    
    SNAKE.move()
   
    if SNAKE.head.distance(FOOD) < 15:
        FOOD.refresh()
        SCORE.increase_score()
        SNAKE.extend()

    if SNAKE.head.xcor() > 280 or  SNAKE.head.xcor() < -280 or SNAKE.head.ycor() > 280 or SNAKE.head.ycor() < -280:
        game_is_on= False
        SCORE.game_over()

    for segment in SNAKE.segments:
        if segment == SNAKE.head:
            pass
        elif SNAKE.head.distance(segment) < 10:
            game_is_on =  False
            SCORE.game_over()

screen.exitonclick()