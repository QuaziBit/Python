# -----------------------------------------+
# Olexandr Matveyev                        |
# CSCI 107, Assignment 5                   |
# Last Updated: October 14, 2019           |
# -----------------------------------------|
# This program computes monthly payments   |
# based on the this formula:               | 
# payment = (i * p) / [ 1 - (1 + i)^{-n} ] |
# where p: principal,                      |
# n: total number of payments, and         |
# i: monthly interest rate                 |
# ( [1/12] of the annual rate)             |
# -----------------------------------------+

""" 
Enter the cost of the car: 15500
Enter amount you have saved: 500
Enter yearly interest rate: .045
Enter total number of payments: 48
Your monthly payment will be $342.05 
"""

cost = input("Please enter the cost of the car: ")
saved = input("Please enter amount you have saved: ")
i = input("Please enter yearly interest rate: ")
n = input("Please enter total number of payments: ")

cost = float(cost)
saved = float(saved)
i = float(i)
n = float(n)

def compute(cost, i, n):

    # getting monthly interest rate
    i = i * (1/12)

    # this part is responsible for: [ 1 - (1 + i)^{-n} ]
    n = (-1 * n)
    x = (1 + i)
    r = pow(x, n)

    # geting principal
    p = (cost - saved)
    
    # getting payment per month
    payment = (i * p) / (1 - r)

    # return result
    return payment

def main():

    # call compute function to get payment
    payment = compute(cost, i, n)

    # print result
    print("\nYour monthly payment will be $%.2f\n" % (payment) )

# call init function
main()
