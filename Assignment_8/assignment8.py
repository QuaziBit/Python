# -----------------------------------------+
# Olexandr Matveyev                        |
# CSCI 107, Assignment 8                   |
# Last Updated: November 09, 2019          |
# -----------------------------------------+
# This program prompts user to input string|
# of colors, like bbb or rbr. Where        |
# b = blue and r = red.                    |
# After, this program will count number of |
# each color in a string and will print    |
# some output based on assignment          |
# instructions.                            | 
# -----------------------------------------+


def three_blues(input_str):

    return_val = False
    count = 0

    for s in input_str:
        if s == "b":
            count = count + 1

    if count == 3:
        return_val = True

    return return_val

def same_amount_of_both(input_str):

    return_val = False
    count_b = 0
    count_r = 0

    for s in input_str:
        if s == "b":
            count_b = count_b + 1
        elif s == "r":
            count_r = count_r + 1

    if count_b == count_r:
        return_val = True

    return return_val

def all_one_color(input_str):

    return_val = False
    count_b = 0
    count_r = 0

    for s in input_str:
        if s == "b":
            count_b = count_b + 1
        elif s == "r":
            count_r = count_r + 1

    if count_b > 0 and count_r == 0:
        return_val = True
    elif count_r > 0 and count_b == 0:
        return_val = True

    return return_val

def user_input():
    u_input = input("Please enter color pattern where b = blue and r = red: ")
    return u_input

def main():

    input_str = user_input()

    print("\nInput has three blues: %r" % (three_blues(input_str)) )
    print("Input has same amount of both: %r" % (same_amount_of_both(input_str)) )
    print("Input has all one color: %r\n" % (all_one_color(input_str)))

main()