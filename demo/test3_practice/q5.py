s = ""

def userInput():
    user_in = input("Enter a number: ")
    return user_in

def recursion(i, n, user_in):

    global s

    if n == len(user_in):
        s = user_in[i:n].capitalize() 
    else:
        s = s + user_in[i:n]

    if i <= 0:
        return s
    else:
        return recursion( (i - 1), (n - 1), user_in)
    
    
def main():
    print("\n")

    user_in = userInput()

    n = len(user_in)
    index = n - 1

    tmp_str = recursion(index, n, user_in)

    n1 = int(user_in)
    n2 = int(tmp_str)
    n3 = n1 + n2

    print("%d + %d = %d\n" % (n1, n2, n3) )

main()