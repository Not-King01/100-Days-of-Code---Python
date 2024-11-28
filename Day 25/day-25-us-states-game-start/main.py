import turtle, pandas
screen = turtle.Screen()

img = "blank_states_img.gif"
screen.addshape(img)

turtle.shape(img)

data = pandas.read_csv('50_states.csv')
states = data.state.to_list()
guessed_data = []

while len(guessed_data) < 50:
    user_input = screen.textinput(f"{len(guessed_data)}/50 States Correct", "What's another state's name? ").title()
    if user_input in states and user_input not in guessed_data:
        guessed_data.append(user_input)
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        a = data[data.state == user_input]
        t.goto(a.x.item(), a.y.item())
        t.write(user_input)

    if user_input == "Exit":
        missing_states = [state for state in states if state not in guessed_data]
        missing_states_df = pandas.DataFrame(missing_states)
        missing_states_df.to_csv("states_to_learn.csv")
        break

