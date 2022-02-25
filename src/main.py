import turtle
import pandas

data = pandas.read_csv("Assets/50_states.csv")
stateList = data.state.to_list()
xcorList = data.x.to_list()
ycorList = data.y.to_list()
screen = turtle.Screen()
screen.title("US:STATES GAME")
screen.setup(width=725, height=491)
image = "Assets/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
writer = turtle.Turtle()
writer.penup()
writer.hideturtle()
gameON = True
correct_guesses = 0
correct_states = []
missed_states=[]
while gameON:
    answer_state = (
        screen.textinput(title=f"{correct_guesses}/50  Guess the state", prompt="Guess the next state")).lower()
    for i in range(len(stateList) - 1):
        try:
            if answer_state == stateList[i].lower():
                writer.goto(xcorList[i], ycorList[i])
                writer.write(stateList[i], font=("Arial", 10, "normal"))
                correct_guesses += 1
                correct_states.append(stateList[i])
        except AttributeError:
            print("ERROR")
        if correct_guesses >= 50:
            gameON = False
        if answer_state.lower() == "exit":
            gameON = False
            if stateList[i] not in correct_states:
                missed_states.append(stateList[i])
                missed_states_dic={
                    "States":missed_states,
                }
                (pandas.DataFrame(missed_states_dic)).to_csv("Assets/missed_states.csv")
screen.exitonclick()
