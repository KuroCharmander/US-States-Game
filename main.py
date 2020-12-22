import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# To get the coordinates of the states
# def get_mouse_click_coor(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()
t = turtle.Turtle()
t.penup()
t.hideturtle()

data = pandas.read_csv("50_states.csv")
state_list = data.state.to_list()
guessed_states = []

while len(guessed_states) < len(data):
    answer_state = screen.textinput(title=f"{len(guessed_states)}/{len(data)} States Correct",
                                    prompt="What's another state's name?").title()
    if answer_state == "Exit":
        missing_states = pandas.DataFrame(state_list)
        missing_states.to_csv("states_to_learn.csv")
        break
    if answer_state in data.values:
        state = data[data["state"] == answer_state]
        if answer_state not in guessed_states:
            t.goto(int(state.x), int(state.y))
            t.write(answer_state)
            guessed_states.append(answer_state)
            state_list.remove(answer_state)
