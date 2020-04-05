# -----------------------------------------+
# Olexandr Matveyev                        |
# CSCI 107, Assignment 2                   |
# Last Updated: September 11, 2019         |
# -----------------------------------------|
# This program should accept user input:   |
# first name, last name, telephone number. |
# After, it should print business card     |
# with entered information.                |
# -----------------------------------------+

# init user-input variables
# ---------------------------------------------------------------------------------- #
fname = input("Please enter your first name > ")
lname = input("Please enter your last name > ")

phone = input("Please enter your telephone number > ")
email = input("Please enter your email > ")
# ---------------------------------------------------------------------------------- #

# we have to warn user that input was invalid partially
# and full name will be truncated
# ---------------------------------------------------------------------------------- #
if len(fname) > 9:
    print("first name should has no more than 9 characters: name will be truncated")
    tmp_fname = ""
    index = 0
    for c in fname:
        if index > 9:
            break
        tmp_fname += c
        index += 1
    fname = tmp_fname

if len(lname) > 10:
    print("last name should has no more than 10 characters: name will be truncated")
    tmp_lname = ""
    index = 0
    for c in lname:
        if index > 10:
            break
        tmp_lname += c
        index += 1
    lname = tmp_lname

# Generating proper amount of spaces after full name
# ---------------------------------------------------------------------------------- #

# len("+------------------------------------------------+") = 50
# name starts at 16
# phone and email starts at 8

# 's' is total available length of characters in the business card
s = "+------------------------------------------------+"

full_name = lname + ", " + fname
i = 16 + len(full_name)
i = len(s) - i -1

index = 0
while index < i:
    full_name += " "
    index += 1
# ---------------------------------------------------------------------------------- #

# checking phone number and email length
# ---------------------------------------------------------------------------------- #
# lmax is maximum available length for phone and email combined
lmax = len(s) - 8

max_phone = 14
if len(phone) > max_phone:
    print("phone number is too large to display")
    phone = "(xxx)-xxx-xxxx"

max_email = len(s) - 8 - max_phone
if len(email) > max_email:
    print("phone number is too large to display")
    email = "champ@snow.com"
# ---------------------------------------------------------------------------------- #

# Generating proper amount of spaces after phone and email
# ---------------------------------------------------------------------------------- #
# lmax is maximum available length for phone and email combined
work = phone + " @: " + email
j = 8 + len(work)
j = len(s) - j - 1

index = 0
while index < j:
    work += " "
    index += 1

# ---------------------------------------------------------------------------------- #

# Output
# ---------------------------------------------------------------------------------- #
info = """
+------------------------------------------------+
|                                                |
| _[_]_                                          |
| (*'*)         %s|
| ( : )         Snow Flurry Developers           |
| ( : )                                          |
|               4 FrostBite Plaza                |
| *****            STE 1400                      |
|               Bozeman, MT 59718                |
|                                                |
| Work: %s|
+------------------------------------------------+  
""" % (full_name, work)

print(info)
# ---------------------------------------------------------------------------------- #