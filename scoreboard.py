from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(-5, 180)
        self.hideturtle()
    
    def show_score(self):
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Arial", 22, "bold"))
    
    def update_score(self):
        self.score += 1
    
    def game_over(self):
        self.goto(0, 0)
        self.screen.bgcolor("green")
        self.write("Game Over", align="center", font=("Arial", 18, "bold"))