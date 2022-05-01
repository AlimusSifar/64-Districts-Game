import turtle
import pandas as pd

image = "./assets/bangladesh.gif"

screen = turtle.Screen()
screen.title("Guess the Division Game")
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv("./assets/64_divisions.csv")
div_names = data.division.to_list()
alt_names = data.alternative.to_list()
guessed_names = []

while len(guessed_names) < len(div_names):
    def match(answer):
        if answer in alt_names:
            return data[data.alternative == answer]
        else:
            return data[data.division == answer]

    answer = screen.textinput(f"{len(guessed_names)}/{len(div_names)} divisions correct", "Guess a division:")
    if not answer:
        break
    answer = answer.title()
    matched = match(answer)
    if matched.empty:
        print("Wrong")
    else:
        div_name = matched.division.item()
        if div_name in guessed_names:
            continue
        guessed_names.append(div_name)
        t = turtle.Turtle(visible=False)
        t.penup()
        t.goto(int(matched.x), int(matched.y))
        t.write(div_name, font=("Arial", 10, "bold"))

turtle.mainloop()
