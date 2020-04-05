# -----------------------------------------+
# Olexandr Matveyev                        |
# CSCI 107, Assignment 9                   |
# Last Updated: November 09, 2019          |
# -----------------------------------------+
# This python program computes Fibonacci   |
# Sequence by using recursion approach and |
# loop in order to print Fibonacci Value   |
# for each 'k' value.                      |
# -----------------------------------------+

# Computing Fibonacci Sequence for each 'k' value
def fibonacci_sequence(k):

    # for 0 and 1 'k' return 1, else do recurrence call of this function
    if k <= 1:
        return 1
    elif k > 1:
        f = fibonacci_sequence(k - 1) + fibonacci_sequence(k - 2)
        return f

# run program
def run(n):
    output = ""

    # loop 'n' times to computing Fibonacci Sequence for each 'k' value
    for k in range(n):
        f = fibonacci_sequence(k)

        # store output as string
        output = output + ("%d " % (f) )
    
    # print result
    print("%s" % (output) )

def main():
    # get input
    n = input("Enter n: ")

    # convert string to int
    n = int(n)

    # start program
    run(n)

# entry point
main()