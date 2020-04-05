# --------------------------- #
# Olexandr Matveyev           #
# Question 1                  #
# --------------------------- #

inDollars = input("How much is the bike in dollars? ")
inDollars = float(inDollars)

haveDollars = input("How many dollars do you have now? ")
haveDollars = float(haveDollars)

result = (inDollars - haveDollars) / 12
print("You must save $%.2f a month to buy the bike in a year.\n" % (result) )