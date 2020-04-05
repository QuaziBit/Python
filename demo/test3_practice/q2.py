def userInput():
    user_in = input("Enter string: ")
    return user_in

def main():
    print("\n")

    user_in = userInput()

    n = len(user_in)
    i = 1
    while i < n:
        tmp_str = ""
        for c in user_in[i:n]:
            tmp_str = tmp_str + c
        print("%s" % (tmp_str) )
        tmp_str = ""
        i = i + 1

    print("\n")

main()