class Rectangle:
    rects = [ ]
    def __init__(self, width, length):
        self.width = width
        self.length = length
        self.rects.append((self.width, self.length))
        
rect1 = Rectangle(2,8)
rect2 = Rectangle(21,11)
rect4 = Rectangle(256,144)
print(Rectangle.rects)
