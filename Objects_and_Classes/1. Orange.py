class Orange:
    def __init__(self, w, c):
        self.color = c
        self.weight = w
        self.mold = 0

    def rot(self, d, t):
        self.mold = d*t

or1 = Orange(150, "dark")
print(or1.mold)
or1.rot(25, 40)
print(or1.mold)