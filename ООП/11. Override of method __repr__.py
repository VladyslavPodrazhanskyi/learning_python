# Override of method __repr__
class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __repr__(self):
        message = "Cat's name is {}, it's age is {}".format(self.name, self.age)
        return message


my_cat = Cat('Murzik', 7)
print(my_cat)