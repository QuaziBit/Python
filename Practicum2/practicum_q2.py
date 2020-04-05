import math

def calcCircumference(r):
    result = 2 * math.pi * r
    return result

def calcArea(r):
    result = math.pi *  (r * r)
    return result

def main():
    radius = input("Enter radius of a circle: ")
    radius = float(radius)

    c = calcCircumference(radius)
    a = calcArea(radius)

    print("The circumference is %.2f, the area is %.2f\n" % (c, a) )

main()
