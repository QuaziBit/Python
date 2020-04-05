# -----------------------------------------+
# Olexandr Matveyev                        |
# CSCI 107, Assignment 2                   |
# Last Updated: September 11, 2019         |
# -----------------------------------------|
# This program should will draw smiley     |
# face with python turtle library.         |
# -----------------------------------------+

# we including python library
import turtle

# init window
# ------------------------------------------- #
# Set up the window and its attributes
wn = turtle.Screen()              

# Set up window size and color
wn.screensize(250, 250, "#F5F5DC")
wn.title("T800 :)")
# ------------------------------------------- #

# radius variable
rad = 100

# init turtle
# ------------------------------------------- #
# Creating turtle object
myTurtle = turtle.Turtle()
# ------------------------------------------- #

# start drawing geometrical shapes
# ------------------------------------------- #
# center circle around origin
myTurtle.up()

# change circle position, center it
myTurtle.goto(0, -100)
myTurtle.down()

# draw head
# ------------------------------------------- #
# draw head
myTurtle.begin_fill()     

# fill it with color
myTurtle.fillcolor("#D2691E") 

# dra circle with radius: rad
myTurtle.circle(rad)
myTurtle.end_fill()
# ------------------------------------------- #

# move cursor to different screen spot without drawing
# ------------------------------------------- #
myTurtle.up()
myTurtle.goto(-67, -40)
myTurtle.setheading(-60)

# thickness of line
myTurtle.width(4)        
myTurtle.down()
# ------------------------------------------- #

# draw smile
# ------------------------------------------- #
myTurtle.circle(80, 160) 

# smile color
myTurtle.color("#FAEBD7")
# ------------------------------------------- #

# draw eyes
# ------------------------------------------- #
myTurtle.fillcolor("#F5F5DC")

for i in range(-35, 105, 70):
    myTurtle.up()

    # change cursor position
    myTurtle.goto(i, 35)

    myTurtle.setheading(0)
    myTurtle.down()
    myTurtle.begin_fill()

    # draw eyes with radius 10
    myTurtle.circle(10)
    myTurtle.end_fill()

# ------------------------------------------- #

# hide pointed
myTurtle.hideturtle()

# window will have close button, so it will wait till user close it
wn.exitonclick()