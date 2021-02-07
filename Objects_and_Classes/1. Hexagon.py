class Hexagon:
    def __init__(self, s1, s2, s3, s4, s5, s6):
        Hexagon.side1 = s1
        Hexagon.side2 = s2
        Hexagon.side3 = s3
        Hexagon.side4 = s4
        Hexagon.side5 = s5
        Hexagon.side6 = s6
    def perimeter(self):
        return (Hexagon.side1+Hexagon.side2+Hexagon.side3+
                Hexagon.side4+Hexagon.side5+Hexagon.side6)
h = Hexagon(3,3,3,4,4,4)
print(h.perimeter())
