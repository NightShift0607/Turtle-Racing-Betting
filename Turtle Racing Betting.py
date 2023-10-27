from turtle import Turtle, Screen
from random import randint

screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput("Make Your Bet", "Which turtle will win the race? Enter a color: ")
color = ["red", "orange", "yellow", "green", "blue", "purple"]
racers = []

for i in range(6):
    tim = Turtle("turtle")
    tim.color(color[i])
    tim.penup()
    tim.goto(-240,(-100 + i * 40))
    racers.append(tim)


if user_bet:
    flag = True


while flag:
    for turtle in racers:
        if turtle.xcor() > 230:
            flag = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        rand_dist = randint(0,10)
        turtle.forward(rand_dist)


screen.exitonclick()