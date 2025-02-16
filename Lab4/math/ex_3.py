import math
side=int(input("Number of sides: "))
length=float(input("length of a side: "))
print("Area of the poligon is: ", round((side*length*length)/(4*math.tan(math.pi/side)), 3))