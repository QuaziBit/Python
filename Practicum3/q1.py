# Olexandr Matveyev

def userInput():
    n = input("Enter a number: ")
    n = int(n)
    return n

def main():
    isDivisible = False
    
    while isDivisible == False:
        n = userInput()
        tmp = n % 7

        if tmp == 0:
            print("%d is divisible by 7\n" % (n) )
            isDivisible = True 

main()

    