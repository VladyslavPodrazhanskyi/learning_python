class AlwaysPositive:
    def __init__(self, n):
        self.number = n
    def __add__(self,other):
        return abs(self.number+other.number)
x = AlwaysPositive(5)
y = AlwaysPositive(-6)
print(x+y)

