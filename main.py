from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


window = Screen()
window.setup(width=600, height=450, startx=140, starty=15)
window.bgcolor("black")
window.tracer(0)
window.title("Snake Game")


snake = Snake()
food = Food()
score = Scoreboard()

speed_stage = 6
speed = 0.07
game_on = True
while game_on:
    snake.move_snake()
    window.update()
    time.sleep(speed)
    score.show_score()
    window.listen()
    window.onkey(snake.up, "Up")
    window.onkey(snake.down, "Down")
    window.onkey(snake.right, "Right")
    window.onkey(snake.left, "Left")
    if snake.head.distance(food) < 10:
        food.appear()
        snake.extend()
        score.update_score()
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 210 or snake.head.ycor() < -210:
        game_on = False
        score.game_over()    
    for segment in snake.turtles[:len(snake.turtles) - 1]:
        if segment.distance(snake.head) < 5:
            game_on = False
            score.game_over()
    if score.score > speed_stage:    
        speed = 0.01 if speed <= 0.020000000000000004 else speed - 0.01
        speed_stage += 6
    

window.exitonclick()