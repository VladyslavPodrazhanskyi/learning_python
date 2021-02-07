# Необязательная агрегация
# Объект класс Person, станет атрибутом класса Dog as Owner
# Агрегация не прописана явна при описании классв,
# Агрегация возникает, когда мы создаем объекта dog1, и в обязательный атрибут owner
# объекта класса DOG указываем объекта класса Person.
# Объект dog2 класса DOG создан без агрегации.

class Person:
    def __init__(self, name, age=25):
        self.name = name
        self.age = age

class Dog:
    def __init__(self, name, age, breed, owner):
        self.name = name
        self.age = age
        self.breed = breed
        self.owner = owner


    def sit(self):
        '''Собака садится по команде'''
        print(self.name.title() + " is now sitting" )
    def roll_over(self):
        '''Собака перекатывается по команде'''
        print(self.name.title() + "is rolled over!")

mick = Person("Mick", 42)
dog1 = Dog('Tobik', 5, "Alabai", mick)
print(dog1.name, dog1.age)
dog1.sit()
dog1.roll_over()
print(dog1.owner.age)

dog2 = Dog("Barbos", 3, "Sheepdog", "Negro")
print(dog2.owner)
