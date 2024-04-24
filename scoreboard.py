from turtle import Turtle

FONT = ('Courier', 20, 'italic')

ALIGN = "center"


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as file:
            self.high_score = file.read()
        self.penup()
        self.goto(0, 280)
        self.color("white")
        self.style = ('Courier', 20, 'italic')
        self.update_score()
        self.hideturtle()
        file.close()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.high_score}", font=FONT, align=ALIGN)

    def get_Score(self):
        self.score += 1
        self.update_score()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("Game Over!", font=FONT, align=ALIGN)

    def reset(self):
        if self.score > int(self.high_score):
            self.high_score = self.score
        with open("data.txt", mode="w") as file:
            file.write(f"{self.high_score}")
        self.score = 0
        self.update_score()
        file.close()
