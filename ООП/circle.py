from math import pi
class Circle:
    def __init__(self, r):
        Circle.radius = r
    def area(self):
        return pi*(Circle.radius)**2
    def diameter(self):
        return Circle.radius*2

circle1 = Circle(10)
print('Area =', circle1.area(), ', Diameter = ', circle1.diameter(), )
