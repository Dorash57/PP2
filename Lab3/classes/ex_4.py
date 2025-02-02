import math

class Point:
    def __init__(self, x0, y0):
        self.x=x0
        self.y=y0

    def show(self):
        print(f"Coordinate: ({self.x}, {self.y})")
    
    def move(self, x1, y1):
        self.x=x1
        self.y=y1

    def dist(self, other_point):
        distance=math.sqrt((other_point.x-self.x)**2+(other_point.y-self.y)**2)
        print(f"Distance between the points: {distance}")

#Fist point
x0=int(input("Fist point x: "))
y0=int(input("Fist point y: "))
point1=Point(x0, y0)

point1.show()

#Move (First point)
new_x0=int(input("New x for first point: "))
new_y0=int(input("New y for first point: "))
point1.move(new_x0, new_y0)

point1.show()

#Second point
x1=int(input("Second point x: "))
y1=y0=int(input("Second point y: "))
point2=Point(x1, y1)

point2.show()

#Distance
point1.dist(point2)