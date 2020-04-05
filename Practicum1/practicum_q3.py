# --------------------------- #
# Olexandr Matveyev           #
# Question 3                  #
# --------------------------- #

import turtle
wn = turtle.Screen()
wn.screensize(250, 250, "black")
wn.title(":)")

line = turtle.Turtle()
line.color("white")
line.width(4)
line.down()
line.fillcolor("green") 
line.begin_fill()
line.right(45)
line.forward(100)
line.right(90)
line.forward(100)
line.right(90)
line.forward(100)
line.right(90)
line.forward(100)
line.end_fill()


line.hideturtle()
wn.exitonclick()