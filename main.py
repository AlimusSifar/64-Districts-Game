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
    if answer in guessed_names:
        continue
    matched = match(answer)
    if matched.empty:
        print("Wrong")
    else:
        guessed_names.append(answer)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(int(matched.x), int(matched.y))
        t.write(matched.division.item(), font=("Arial", 10, "bold"))

turtle.mainloop()
