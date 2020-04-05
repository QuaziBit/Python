# -----------------------------------------+
# Olexandr Matveyev                        |
# CSCI 107, Assignment 10                  |
# Last Updated: November 29, 2019          |
# -----------------------------------------+
# This program lines up each sentens       |
# on a single line, and adds extra spaces  |
# before each quotation mark.              |
# -----------------------------------------+

def run(fileName):

    # open file
    textFile = open(fileName, "r")

    output1 = ""
    has_q_mark = False
    # read text line by line and place each sentens on a single line 
    for l in textFile:
        tmp_str = ""
        for s in l:
            if s != ".":
                if s == "\n":
                    s = ""
                tmp_str = tmp_str + s
            elif s == ".":
                tmp_str = tmp_str + "." + "\n"
                
        output1 = output1 + tmp_str
        tmp_str = ""

    output2 = ""
    # read formated text line by line and add extra spaces in front of each quotation mark
    for l in output1:
        tmp_str = ""
        for s in l:
            if s == "\"" and has_q_mark == False:
               s = "     \""
               has_q_mark = True
            tmp_str = tmp_str + s

        output2 = output2 + tmp_str
        tmp_str = ""
        has_q_mark = False
    

    print("%s\n" % (output2) )


def main():
    run("tale.txt")

main()
