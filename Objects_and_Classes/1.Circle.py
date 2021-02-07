class Circle:
    def __init__(self, r):
        self.radius = r
    def area(self):
        from math import pi
        return pi*(self.radius)**2
    def change_rad(self, new_rad):
        self.radius = new_rad


my_circle = Circle(24)
print(my_circle.area())
my_circle.change_rad(150)
print(my_circle.area())
