from math import sqrt
class Triangle:
    def __init__(self, side1, side2, side3):
        Triangle.side1 = side1
        Triangle.side2 = side2
        Triangle.side3 = side3
    def halfperimeter(self):
        return (Triangle.side1+Triangle.side2+Triangle.side3)/2
    def area(self):
# при описании метода с использование уже описанного метода внутри:
# во внутреннем методе нужно указывать параметр self
        return sqrt(Triangle.halfperimeter(self)*(Triangle.halfperimeter(self)-Triangle.side1)*
                    (Triangle.halfperimeter(self)-Triangle.side2)*(Triangle.halfperimeter(self)-Triangle.side3))
tr = Triangle(3,4,5)
print(tr.area())
print(tr.halfperimeter())
