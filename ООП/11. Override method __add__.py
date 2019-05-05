# Override of method __add__

class ModulesAdding:
    def __init__(self, n):
        self.number = n

    def __add__(self, other):
        return abs(self.number) + abs(other.number)


a = ModulesAdding(-5)
b = ModulesAdding(-4)
print(a+b)
