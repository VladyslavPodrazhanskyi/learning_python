class Square:
    square_list = [ ]
    def __init__(self, side):
        self.side = side
        self.square_list.append(self)
    def area(self):
        return self.side**2
    def __repr__(self):
        return '{0} на {0} на {0} на {0}'.format(self.side)
    
    def equal_check(self, other):
        if self is other:
            return True
        else:
            return False

s1 = Square(25)
s2 = Square(22)
s3 = Square(21)
s4 = Square(26)
s5 = Square(2)
s6 = s2

print(Square.equal_check(s2,s6))


