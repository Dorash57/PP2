class Shape:
    def area(self):
        print('0')
    
class Square(Shape):
    def __init__(self, length):
        self.length=length


    def area(self):
        print("Area:", self.length**2)
    
my_shape=Shape()
my_shape.area()

square_length=float(input("square_length: "))
my_square=Square(square_length)
my_square.area()