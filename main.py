import turtle
import pandas as pd

from name_tag import Tags

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
game_is_on = True
turtle.shape(image)

score = 0
guessed = []

data = pd.read_csv("50_states.csv")
# TODO 1 convert the state name to list
states_list = data.state.to_list()
print(states_list)
while len(guessed) < 51:
    user_input = screen.textinput(f"{score}/50 States Correct", "Please input a state name:").title()

# TODO not in and break fuction
    if user_input == "Exit":
        missing_states = []
        for states in states_list:
            if states not in guessed:
                missing_states.append(states)
# TODO save the list to data frame then print to csv
        new_data=pd.DataFrame(missing_states)
        new_data.to_csv("states to learn.csv")
        break
    else:
        for g in guessed:
            if user_input == g:
                user_input = screen.textinput(f"{user_input} already guessed", "Please input another state name:").title()

        for n in data.state:
            if user_input == n:
                # TODO 1: if correct, create new turtle then go to the xy cor as provided
                stat_data = (data[data.state == user_input])
                cor_x = int(stat_data.x)
                cor_y = int(stat_data.y)
                name_tag = Tags(user_input, cor_x, cor_y)
                score += 1
                guessed.append(user_input)
