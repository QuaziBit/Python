# [4]
import math

def main():
    n = input("n: ")
    r = input("r: ")
    n = int(n)
    r = int(r)

    combinations = math.factorial(n) / ( math.factorial((n - r)) * math.factorial(r) )

    print("C(%d,%d): %d\n" % (n,r,combinations) )


main()


# [3]
"""
import math

def approxFactorial(n):
    out = pow( (2 * math.pi * n), 0.5) * pow( (n / math.e), n)
    return out

def getFactorial(n):

    factorial = n
    while n >= 1:
        if (n - 1) >= 1:
            factorial = factorial * (n - 1)
        n = n - 1

    return factorial

def main():
    n = input("n: ")
    n = int(n)

    approx = approxFactorial(n)
    factorial = getFactorial(n)

    print("Approximation factorial of %d is %.2f\n" % (n, approx) )
    print("factorial of %d is %d\n" % (n, factorial) )

main()
"""


# [2]
"""
from math import gcd

def getGcd(a, b):
    return gcd(b, a)

def main():
    counter = 1

    while counter <= 4:
        a = input("a: ")
        b = input("b: ")

        a = int(a)
        b = int(b)
        tmp = getGcd(a, b)
        print("The greatest common divisor for %d and %d is %d\n" % (a, b, tmp) )

        counter = counter + 1


main()
"""




# [1]
"""
import random

def getRandom(min, max):
    return random.randint(min, max)


def main():
    r_sum = 0.0
    avg = 0.0
    i = 1

    while i <= 50:
        r = getRandom(1, 100)
        r_sum = r_sum + (r * r)
        i = i + 1

    avg = r_sum / 50
    print("avg: %.2f\n" % (avg) )

main()
"""