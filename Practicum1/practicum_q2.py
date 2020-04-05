# --------------------------- #
# Olexandr Matveyev           #
# Question 2                  #
# --------------------------- #

name = input("Enter your name: ")
field = input("Enter the field width: ")
field = int(field)

i = 0
left = (field -1) - len(name) - 1
spc = ""
dash = ""

while i < left:
    spc += " "
    i = i + 1

i = 0
while i < (field - 1):
    dash += "-"
    i = i + 1 

output_str = """
+%s+
|%s%s |
+%s+
""" % (dash, spc, name, dash)

print(output_str)

