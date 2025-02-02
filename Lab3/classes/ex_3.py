class Shape:
    def area(self):
        print(0)
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length=length
        self.width=width
    
    def area(self):
        print("Area:", self.width*self.length)

rect_length=float(input("Length: "))
rect_width=float(input("Width: "))
my_square=Rectangle(rect_length, rect_width)
my_square.area()