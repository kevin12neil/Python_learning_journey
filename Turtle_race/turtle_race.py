import turtle as t
import random

colors = ["red", "orange", "yellow", "green", "blue", "violet"]

y_pos = [-100, -60, -20, 20, 60, 100]

all_turtles = []

race_on = False

screen = t.Screen()
screen.setup(width = 600, height = 400)
user_input = screen.textinput(title = "Make your bet", prompt = "Which turtle will iwn the race? pick a color (red, orange, yellow, green, blue, violet): ")

for i in range(6):
    new_turtle = t.Turtle()
    new_turtle.shape("turtle")
    new_turtle.penup()
    new_turtle.color(colors[i])
    new_turtle.goto(-280, y_pos[i])
    all_turtles.append(new_turtle)

if user_input:
    race_on = True


winner = ""

while race_on:
    for turtle in all_turtles:
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)
        if turtle.xcor() >= 280:
            winner = turtle.color()[0]
            race_on = False
            break

if user_input and user_input.lower() != winner:
    print("You lose.")
else:
    print("You Win!")
print(f"The winner is {winner}.")
    




screen.exitonclick()
