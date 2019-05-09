class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

dog = Dog("Barbos", 11)
print(hash(dog))
print(type(dog) is Dog)