# -----------------------------------------+
# Olexandr Matveyev                        |
# CSCI 107, Practicum                      |
# Last Updated:                            |
# -----------------------------------------|
# -----------------------------------------+

# Q1
"""
number = input("Enter a positive integer from 1 to 9: ")

number = int(number)
counter = 1
s = ""

while counter <= number:
    print("%s%s" % (s, counter) )
    s += " "
    counter = counter + 1

print("\n")
"""

# Q2
import turtle
wn = turtle.Screen()
wn.screensize(250, 250, "#F5F5DC")
wn.title("Spider")

line = turtle.Turtle()
line.color("green")
line.width(2)
line.down()
line.forward(100)
line.backward(50)
line.right(90)
line.forward(50)
line.backward(50)
line.right(180)
line.forward(50)
line.backward(50)
line.right(45)
line.forward(50)
line.backward(100)
line.forward(50)
line.right(90)
line.forward(50)
line.backward(100)
line.forward(50)


line.hideturtle()
wn.exitonclick()


# Q3
"""
a = input("Enter a: ")
b = input("Enter b: ")
a = float(a)
b = float(b)
x = -1 * b / a
print("The equation ax + b = 0 when x = %.1f\n" % (x) )
"""

# Addition Q
"""
money = input("How much money do you want to save for the laptop? ")
money = float(money)

perMonth = input("How much can you save a month? ")
perMonth = float(perMonth)

result = money / perMonth
print("You can buy the laptop in %.2f\n" % (result) )
"""








