class Animal:
    __pets = {}

    def __new__(cls, name):
        if name in cls.__pets:
            print("Pet with the same name is already exists!")
            return cls.__pets[name]
        print("New pet")
        return super(Animal, cls).__new__(cls)

    def __init__(self, name):
        self.name = name
        type(self).__pets[name] = self

    @classmethod
    def all_pets(cls):
        for item in cls.__pets:
            print(item)

    def update_info(self, item_dict):
        for item in item_dict.items():
            setattr(self, item[0], item[1])


cat = Animal('Tom')
dog = Animal('Jack')

a3 = Animal("Tom")

Animal.all_pets()

print(a3 is cat)