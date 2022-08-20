from turtle import Turtle, Screen
import random

in_race = False

screen = Screen()
screen.setup(width=700, height=600)
user_bet = screen.textinput(title= "Make your bet !", prompt="Which turtle will win the race? \n red \n orange \n yellow \n green \n blue \n purple \n"
                                                             "Enter a color: ")

y_coordinates = [-50, 0, 50, 100, 150, 200]
colours = ["red", "orange", "yellow", "green", "blue", "purple"]

turtles = []
for i in range(0, 6):
    tim = Turtle(shape="turtle")
    tim.penup()
    tim.color(colours[i])
    tim.goto(x = - 330, y = y_coordinates[i])
    turtles.append(tim)

#As soon as the player enters their bet
if user_bet:
    in_race = True

while in_race:

    for turtle in turtles:
        if turtle.xcor() > 330:
            colour = turtle.pencolor()
            if user_bet == colour:
                print(f"You won the bet ! The {colour} turtle won the the race.")
                in_race = False
            else:
                print(f"You lost the bet ! The {colour} turtle won the the race.")
                in_race = False
        distance = random.randint(0, 10)
        turtle.forward(distance)



screen.exitonclick()
