import turtle
import pandas as pd
screen = turtle.Screen()
screen.title('US_States game')
image = 'blank_states_img.gif' ## Pic path
screen.addshape(image)
turtle.shape(image)

data=pd.read_csv('50_states.csv')
all_states = data.state.to_list()
guessed_state = []

while len(guessed_state) < 50:
    answer_state = screen.textinput(title=f'{len(guessed_state)}/50 Guessed correctly', prompt='What the other state name?').title() ## To capitalize first word of names
    missed_states = []
    if answer_state == 'Exit':
        break

    missed_states = [state for state in all_states if state not in guessed_state]
    # for state in all_states:
    #     if state not in guessed_state:
    #         missed_states.append(state)

    new_data = pd.DataFrame(missed_states)
    new_data.to_csv('States to Learn.csv')


    if answer_state in all_states:
        guessed_state.append(answer_state)

        t=turtle.Turtle()
        t.penup()
        t.hideturtle()
        state_data = data[data.state == answer_state]## Getting whole row of answer
        t.goto(int(state_data.x) , int(state_data.y))
        t.write(state_data.state.item())## Return first item in data

screen.exitonclick()

