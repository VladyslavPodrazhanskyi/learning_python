import sys

class Cat:
    def __init__(self, name):
        self.name = name


cat1 = Cat('Barsik')  # I can add any attributes to the cat, but it takes more memory

# cat1.age = 4

# print(cat1.age)
# print(cat1.__dict__)


class DogWithSlots:

    __slots__ = ['name']

    def __init__(self, name):
        self.name = name


dog1 = DogWithSlots('Barbos')  # dog has slots -  limited attribute, but less memory

# dog1.age = 4
#
# # print(cat1.age)
# # print(cat1.__dict__)

print('size cat')
print(sys.getsizeof(cat1))  # 48
print('size dog')
print(sys.getsizeof(dog1))  # 40
