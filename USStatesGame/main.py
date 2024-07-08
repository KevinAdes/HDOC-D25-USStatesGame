from turtle import Turtle, Screen
import pandas

states_data = pandas.read_csv("50_states.csv")
all_states = states_data.state.to_list()
guessed_states = []

map_screen = Screen()
map_screen.setup(725, 491)
map_screen.bgpic("blank_states_img.gif")

run_game = True


while run_game:
    guess = map_screen.textinput(title="Guess", prompt="Enter A State")
    if guess == "quit":
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if guess in all_states:
        newTurtle = Turtle()
        newTurtle.penup()
        newTurtle.hideturtle()
        state = states_data[states_data["state"] == guess]
        as_dict = state.to_dict()
        xpos = as_dict['x'][state.index.values[0]]
        ypos = as_dict['y'][state.index.values[0]]
        newTurtle.teleport(xpos, ypos)
        newTurtle.write(guess, align="left")
        guessed_states.append(guess)

map_screen.bye()
