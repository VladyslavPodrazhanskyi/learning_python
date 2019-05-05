# 1) circles -  attribut of class Circle  -  list of instances Circle
# 2) override method __repr__ and it return message with radius of every instance
# instead of objects when i use print() function

class Circle:
    circles = []
    def __init__(self, r):
        self.radius = r
        Circle.circles.append(self)
    def __repr__(self):
        message = "Circle with radius = " + str(self.radius)
        return message
    def area(self):
        from math import pi
        return pi*(self.radius)**2
    def diameter(self):
        return self.radius*2


circle1 = Circle(10)
circle2 = Circle(54)

for circle in Circle.circles:
    print(circle)
