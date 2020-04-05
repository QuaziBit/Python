# -----------------------------------------+
# Olexandr Matveyev                        |
# CSCI 107, Assignment 7                   |
# Last Updated: November 04, 2019          |
# -----------------------------------------+
# This application asks user to enter      |
# two input valuse cost and isTeacher.     |
# After, it will compute discount          |
# information, and will print it.          |
# -----------------------------------------+

print("")
cost = input("Enter the cost of your items: ")
cost = float(cost)

isTeacher = input("Are you a music teacher (y or n)? ")


def nicePrint(a, b):

    output = ""
    max_length = 50
    a_length = len(a)
    b_length = len(b)

    diff_length = max_length - (a_length + b_length)

    output = a
    for _ in range(diff_length):
        output = output + " "
    output = output + b

    print("%s" % (output) )

def compute(cost, isTeacher):
    option = 0
    discount = 0
    if (isTeacher == "y"):
        option = 1

    if (option == 1):

        if (cost < 100):
            discount = 10.0
        else:
            discount = 12.0

        d = cost / 100.0 * discount
        total_d = cost - d
        sales_tax = total_d / 100.0 * 5.0
        total = sales_tax + total_d

        a = "Total purchases: "
        b = "%.2f" % (cost)
        nicePrint(a, b)

        a = "Teacher’s Discount (%.2f%%): " % (discount)
        b = "%.2f" % (d)
        nicePrint(a, b)

        a = "Discounted Total: "
        b = "%.2f" % (total_d) 
        nicePrint(a, b)

        a = "Sales Tax (5%) "
        b = "%.2f" % (sales_tax)
        nicePrint(a, b)

        a = "Total "
        b = "%.2f"  % (total)
        nicePrint(a, b)

    else:
        
        sales_tax = cost / 100.0 * 5.0
        total = sales_tax + cost

        a = "Total purchases: "
        b = "%.2f" % (cost)
        nicePrint(a, b)

        a = "Sales Tax (5%) "
        b = "%.2f" % (sales_tax)
        nicePrint(a, b)

        a = "Total "
        b = "%.2f"  % (total)
        nicePrint(a, b)



def main():
    print("")
    compute(cost, isTeacher)
    print("")

main()