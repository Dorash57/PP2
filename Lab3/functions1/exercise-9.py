import math
def volume_of_sphere(r):
    V=4/3*math.pi*r**3
    print(round(V, 2))

Radius=float(input("Radius: "))
volume_of_sphere(Radius)