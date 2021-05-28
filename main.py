from turtle import Screen
import time
from snake import Snake
from food import Food
from score import Score

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("snake game")
screen.tracer(0)
tim = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(tim.up, "Up")
screen.onkey(tim.down, "Down")
screen.onkey(tim.left, "Left")
screen.onkey(tim.right, "Right")
screen.onkey(exit, "z")
game = True
while game:
    screen.update()
    time.sleep(0.1)
    tim.snake_move()
    # detect collusion with food
    if tim.head.distance(food) < 15:
        food.refresh()
        score.add_score()
        tim.extend()
    # detect the wall
    if tim.head.xcor() > 280 or tim.head.xcor() < -280 or tim.head.ycor() > 280 or tim.head.ycor() < -280:
        game = False
        score.game_over()
    # detect the tail
    for segment in tim.sequence[1:]:
        if tim.head.distance(segment) < 10:
            game = False
            score.game_over()

screen.exitonclick()
