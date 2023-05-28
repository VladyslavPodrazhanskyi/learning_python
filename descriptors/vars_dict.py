class Cat:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __str__(self):
        return f'Cat with name: {self.name}, age: {self.age}'


# the same
print(Cat.__dict__)
print(vars(Cat))

cat_max = Cat('Max', 4)

print(cat_max.__dict__)
print(vars(cat_max))