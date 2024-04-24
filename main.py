import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()
screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.t_left, "a")
screen.onkey(snake.t_right, "d")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision w food
    if snake.head.distance(food) < 15:

        scoreboard.get_Score()
        snake.extend()
        food.refresh()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:

        scoreboard.reset()
        snake.reset()

    # Detect collision w tail
    if snake.head.position() == snake.segments[-1].position:

        scoreboard.reset()
        snake.reset()

screen.exitonclick()
