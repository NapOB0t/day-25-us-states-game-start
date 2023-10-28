import turtle
import pandas
screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
game_is_on = True
correct_Answer = 0

list_Answers = []
while game_is_on:
    answer_state = screen.textinput(title=f"Guess the state {correct_Answer}/50 left", prompt=
                                    "What's another state name").title()
#Loops through each stat name
    for st in range(0, len(data.state)):
        if answer_state == data.state[st]:
            x_coordinate = data.x[st]
            y_coordinate = data.y[st]
            tim = turtle.Turtle()
            tim.hideturtle()
            tim.penup()
            tim.goto(x_coordinate, y_coordinate)
            tim.write(str(data.state[st]), align='center')
            list_Answers.append(answer_state)
            correct_Answer += 1
        elif correct_Answer == 50:
            turtle.Turtle().write("You won congratulations")
            game_is_on = False

    if answer_state == "exit ":
        break


turtle.mainloop()
