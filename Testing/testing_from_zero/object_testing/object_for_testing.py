class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say(self):
        return 'Myau'

    def sleep(self):
        return 'cat is sleeping'

    def eat(self, food):
        return "cat eats " + food

    def get_older(self, value):
        self.age += value


# cat = Cat('Barsik', 2)
# print(cat.age)
# cat.get_older(5)
# print(cat.age)