class Cat:
    cat_number = 0

    def __init__(self, name, age, breed='unknown'):
        self.name = name
        self.age = age
        self.breed = breed
        Cat.cat_number += 1

    def speak(self):
        print(f'Myau, my name is {self.name}')

    @staticmethod
    def square(diameter):
        return 3.14 * diameter ** 2 / 4

    @classmethod
    def get_numbers(cls):
        return cls.cat_number

    def __add__(self, other):
        return self.age + other.age


print('Cat:', type(Cat))

cat1 = Cat(breed='British', name='Murzik', age=5)
print('cat1:', type(cat1))
print(cat1.name, cat1.age, cat1.breed)
cat1.speak()
print(cat1.square(5))
print(Cat.cat_number)
cat2 = Cat(name='Barsik', age=3)
print(Cat.cat_number)
print(cat1.cat_number)

print(cat1 + cat2)


def speak(some_string):
    print(some_string)


speak('Learn python')

print(len('skfssfsdfkfsjfhkjshfhswrw'))
print('skfssfsdfkfsjfhkjshfhswrw'.__len__())

a = 6
b = -2

print(a + b)
print(a.__add__(b))