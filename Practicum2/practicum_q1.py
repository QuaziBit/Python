import random
def main():
    avg = 0.0
    for i in range(10):
        r = random.randint(1, 20)
        avg = avg + r
        print("%d %d\n" % (r, (r * r * r) ) )
    avg = avg / 10
    print("The average of the numbers: %.2f\n" % (avg) )
main()