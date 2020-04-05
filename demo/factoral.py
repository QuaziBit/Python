n = input("Enter number > ")

n = int(n)
i = n - 1
result = n
while i > 1:
    result = result * i 
    i = i - 1

print(result)