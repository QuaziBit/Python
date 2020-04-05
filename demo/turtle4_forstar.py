import turtle  # importing turtle module/library
gs = turtle.Screen() # creates a graphics window
gs.bgcolor("light pink")
gs.title("My star")
alex = turtle.Turtle()  # starts at 0,0; is black; is 2 pixels wide
alex.pensize(4)
alex.pencolor("blue")
alex.forward(150)

for i in [1, 2, 3, 4]:
    alex.right(144)
    alex.forward(150)



            
