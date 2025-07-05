# Mathew Mckee
# 7/5/2025
# P4Lab1a
# Turtle draw square + triangle

import turtle
turtle.bgcolor("black")
turtle.color("white")

for i in range(4):
    turtle.forward(60)
    turtle.right(90)

turtle.penup()
turtle.left(90)
turtle.forward(60)
turtle.pendown()

for i in range(3):
    turtle.forward(60)
    turtle.right(120)
