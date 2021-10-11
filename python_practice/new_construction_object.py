class Animal:
    __pets = {}

    def __new__(cls, name):
        if name in cls.__pets:
            print('Pet with the same name is already exists!')
            return cls.__pets[name]
        print('New pet')
        return super(Animal, cls).__new__(cls)

    def __init__(self, name):
        self.name = name
        type(self).__pets[name] = self

    @classmethod
    def all_pets(cls):
        for item in cls.__pets.items():
            print(item)

a1 = Animal('Tom')
a2 = Animal('Jack')
a3 = Animal('Tom')

print('My pets:')
Animal.all_pets()

print(a1 is a3 and a1 is not a2)