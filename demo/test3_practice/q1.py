def getSum(n):
    i = 1
    tmp_sum = n
    while i < n:
        tmp_sum = tmp_sum + i
        i = i + 1

    return tmp_sum

def printSum(tmp_sum, n):
    print("The sum of 1 to %d is %d\n" % (n, tmp_sum) )

def main():
    n = input("Enter a number: ")
    n = int(n)

    tmp_sum = getSum(n)
    printSum(tmp_sum, n)

main()