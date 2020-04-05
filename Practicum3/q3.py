# Olexandr Matveyev

def userInput():
    user_in = input("Enter a number that includes 1's: ")
    return user_in

def main():
    user_in = userInput()
    new_str = ""
    i = 0
    while i < len(user_in):
        if user_in[i] == "1":
            new_str = new_str + "2"
        else:
            new_str = new_str + user_in[i]
        i = i + 1

    n1 = int(user_in)
    n2 = int(new_str)
    n3 = n1 + n2
    print("%d + %d = %d\n" % (n1, n2, n3))

main()