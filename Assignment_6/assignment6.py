# -----------------------------------------+
# Olexandr Matveyev                        |
# CSCI 107, Assignment 6                   |
# Last Updated: October 19, 2019           |
# -----------------------------------------|
# NOTE:                                    |
# In the lab description is written that   |
# blocks must have 20 pix size, I changed  | 
# to 50 pixels because my vision ability   |
# is low, so I did change size.            |                              
# -----------------------------------------+
# This application is utilizing turtle API |
# to draw different geometrical shapes,    |
# and for castle from that geometrical     |
# shapes.                                  |
# -----------------------------------------+

# we including python library
import turtle

# this function is use to update drawing cursor location
def update_cursor_location(myTurtle, init_x, init_y):
    
    # update cursor location
    myTurtle.up()
    myTurtle.goto(init_x, init_y)
    myTurtle.down()

# this function is use to draw squares
def dra_single_square(myTurtle, block_size, angle, color):
    counter = 0 
    limit = 4 # corners of square

    # set fill color
    myTurtle.fillcolor(color)

    # start filled in with color
    myTurtle.begin_fill()

    # draw single square
    while counter <= limit:
        myTurtle.forward(block_size)
        myTurtle.left(angle)
        counter = counter + 1

    # end filled in with color
    myTurtle.end_fill()

    # reset angle of turtle
    myTurtle.setheading(0)

# this function is use to draw triangles
def dra_single_triangle(myTurtle, block_size, angle, color):
    counter = 0 
    limit = 4 # corners of square

    # set fill color
    myTurtle.fillcolor(color)

    # start filled in with color
    myTurtle.begin_fill()

    # draw single square
    while counter <= limit:
        myTurtle.forward(block_size)
        myTurtle.left(angle)
        counter = counter + 1

    # end filled in with color
    myTurtle.end_fill()

    # reset angle of turtle
    myTurtle.setheading(0)

# initialize window for this application
def init_wn():
    # init window
    # ------------------------------------------- #
    # Set up the window and its attributes
    wn = turtle.Screen()              

    # Set up window size and color
    wn.screensize(240, 240, "#F5F5DC")
    wn.title("T800 :)")
    # ------------------------------------------- #

    return wn

# create turtle object
def init_Turtle(init_x, init_y):

    # init turtle
    # ------------------------------------------- #
    # Creating turtle object
    myTurtle = turtle.Turtle()
    # ------------------------------------------- #

    # set initial position of the cursor
    update_cursor_location(myTurtle, init_x, init_y)

    return myTurtle


# entry point of this application
def start():

    # initialization
    # ----------------------------------------------------------------------- #
    # initial position of the drawing cursor
    init_x = -200
    init_y = -250

    # init window
    wn = init_wn()

    # init turtel
    myTurtle = init_Turtle(init_x, init_y)
    # ----------------------------------------------------------------------- #

    # initialization of local variables
    # ----------------------------------------------------------------------- #
    # colors
    init_color = "#34495e"
    door_color = "#d35400"
    triangle_color = "#8e44ad"

    # size of a block in pixels
    block_size = 50

    # angle used to specify drawing trajectory for rectangles and triangles
    angle = 90

    # number of blocks in x-diraction
    num_of_blocks_x = 8

    # number of blocks in y-diraction
    num_of_blocks_y = (num_of_blocks_x / 2)

    # counters of x and y blocks
    x_count = 1
    y_count = 1

    # we need to use middle value, it will help us to figure out 
    # were we have to change color of blocks
    x_middle = num_of_blocks_x / 2
    y_middle = num_of_blocks_y / 2
    # ----------------------------------------------------------------------- #

    # draw squares
    # ----------------------------------------------------------------------- #
    while y_count <= num_of_blocks_y:
        while x_count <= num_of_blocks_x:

            # build blocks with different colors
            if y_count <= (y_middle + 1):
                if x_count == x_middle or x_count == (x_middle + 1): 
                    # door color
                    dra_single_square(myTurtle, block_size, angle, door_color)
                else:
                    # base color
                    dra_single_square(myTurtle, block_size, angle, init_color)
            else:
                # base color
                dra_single_square(myTurtle, block_size, angle, init_color)
            x_count = x_count + 1

        # reset x counter
        x_count = 1

        # update cursor location
        init_y = init_y + block_size
        update_cursor_location(myTurtle, init_x, init_y)
        
        y_count = y_count + 1
    # ----------------------------------------------------------------------- #
    
    # reset x counter
    x_count = 1

    # draw triangles
    # ----------------------------------------------------------------------- #
    # left triangle
    angle = 120
    update_cursor_location(myTurtle, init_x, init_y)
    dra_single_triangle(myTurtle, block_size, angle, triangle_color)

    # right triangle
    init_x = init_x + (num_of_blocks_x - 1) * block_size
    update_cursor_location(myTurtle, init_x, init_y)
    dra_single_triangle(myTurtle, block_size, angle, triangle_color)
    # ----------------------------------------------------------------------- #

    # final init for the cursor and window
    # ----------------------------------------------------------------------- #
    # hide pointed
    myTurtle.hideturtle()

    # window will have close button, so it will wait till user close it
    wn.exitonclick()
    # ----------------------------------------------------------------------- #

# run application
start()