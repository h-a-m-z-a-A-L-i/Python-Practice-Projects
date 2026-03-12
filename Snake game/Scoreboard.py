from turtle import Turtle , Screen

class scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.penup()
        self.high_score=0
        with open('data.txt' , mode='r') as file:
            self.high_score = int(file.read())
        self.goto(0,270)
        self.hideturtle()
        self.color('white')
        self.update_score()

    def update_score(self):
        self.clear()

        self.write(f'Score : {self.score} High score : {self.high_score}', align='center' , font=('Arial' , 24 , 'normal'))

    def increase_score(self):
        self.score+=1
        self.clear() ## To clear previous test written by turtle
        self.update_score()

    def reset_score(self):
        if self.score>self.high_score:
            self.high_score = self.score
            with open('data.txt', mode='w') as file:
                file.write(str(self.high_score))
        self.score = 0 ## Order matters
        self.update_score()


    # def game_is_over(self): ## Not needed now
    #     self.goto(0,0)
    #     self.write('Game Over', align='center', font=('Arial', 24, 'normal'))