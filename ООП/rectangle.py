class Rectangle:
    def __init__(self, w, l):
        self.width = w
        self.length = l
        print('created!')
    def area(self):
        return self.width*self.length
    def change(self, w, l):
        self.width = w
        self.length = l

r1 = Rectangle(25, 50)
print(r1.area())
r1.change(12, 2)
print(r1.area())
