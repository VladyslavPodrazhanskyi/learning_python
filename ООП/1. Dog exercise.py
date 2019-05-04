class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def sit(self):
        print(self.name + " is sitting now.")
    def roll_over(self):
        print(self.name + " rolled over")

my_dog = Dog('Bobik', 7)
print(type(my_dog))
my_dog.sit()
my_dog.roll_over()
my_dog.age += 4
print(my_dog.age)