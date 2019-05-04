class AlwaysPositive:
    def __init__(self, number):
        self.number = number
    def __add__(self, other):
        return abs(self.number+other.number)
x = AlwaysPositive(3)
y = AlwaysPositive(4)
print(x+y)
