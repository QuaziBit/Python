import math

def main():
    n = input("Enter number of items in set: ")
    r = input("Enter number of items in subset: ")
    n = int(n)
    r = int(r)

    permutations = math.factorial(n) / math.factorial((n - r))

    print("The number of permutations is %d\n" % (permutations) )


main()