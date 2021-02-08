# https://realpython.com/instance-class-and-static-methods-demystified/

from math import pi

class Pizza:

    def __init__(self, ingridients, diameter=40):
        self.ingridients = ingridients
        self.diameter = diameter

    def __repr__(self):
        return f'Pizza({self.ingridients}, diameter: {self.diameter})'

    @staticmethod
    def circle_area(diameter):
        return pi * (diameter ** 2 / 4)

    def area(self):
        return self.circle_area(self.diameter)

    @classmethod
    def margarita(cls):
        return cls(['mozzarella', 'tomatoes'])

    @classmethod
    def proscurito(cls):
        return cls(['mozzarella', 'tomatoes', 'ham'])


pizza1 = Pizza(['cheese', 'tomatoes'], 25)

m1 = Pizza.margarita()
p1 = Pizza.proscurito()
m2 = pizza1.margarita()
p2 = pizza1.proscurito()

print(pizza1, pizza1.area())
print(m1, m1.area())
print(m2)
print(p1)
print(p2)


# pizza2 = Pizza(['mozzarella', 'tomatoes'])
# pizza3 = Pizza(['mozzarella', 'tomatoes', 'ham', 'mushrooms'])
# pizza4 = Pizza(['mozzarella'] * 4)
#
# print(pizza1)
# print(pizza2)
# print(pizza3)
# print(pizza4)

