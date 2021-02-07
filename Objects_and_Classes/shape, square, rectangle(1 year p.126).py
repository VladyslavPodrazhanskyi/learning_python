from math import pi

class Shape:
    def what_am_i(self):
        print('Я - фигура!')
        
class Rectangle(Shape):
    def __init__(self, width, length):
        self.width = width
        self.length = length
    def perimeter(self):
        return 2*(self.width+self.length)
    
class Square(Shape):
    def __init__(self, length):
        self.length = length
    def perimeter(self):
        return 4*self.length
    def change_size(self, delta):
        self.length += delta
        
class Circle(Shape):
    def __init__(self, r):
        self.radius = r
    def perimeter(self):
        return 2*pi*self.radius
    
my_circle = Circle(54)
my_circle.what_am_i()
print(my_circle.perimeter())

my_rectangle = Rectangle(5,12)
print(my_rectangle.perimeter())
my_rectangle.what_am_i()

my_square = Square(25)
print(my_square.perimeter())
my_square.change_size(-5)
print(my_square.perimeter())
print(my_square.length)
my_square.what_am_i()


my_shape = Shape()
my_shape.what_am_i ()
