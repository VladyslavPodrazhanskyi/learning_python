from imports_solving import Cat, Dog


cat = Cat('Barsik', 4)
dog = Dog('Sharik', 3)

class Zoo:
    def __init__(self, dog, cat):
        self._dog = dog
        self._cat = cat


zoo = Zoo(dog, cat)

print(zoo)