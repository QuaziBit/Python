# Olexandr Matveyev

def userInput():
    user_in = input("Enter string: ")
    return user_in

def recursion(i, n, user_in):

    print("%s" % (user_in[i:n]))

    if n <= 0:
        return ""
    else:
        return recursion( i, (n - 1), user_in)
    
def main():
    print("\n")

    index = 0
    user_in = userInput()

    recursion(index, len(user_in), user_in)

    print("")

main()