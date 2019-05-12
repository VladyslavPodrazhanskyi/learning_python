# По умолчанию класс не является итератором.
# Итерация - поэлементный обход данных.
# iterable class has 2 magic methods __iter__, __next__.
# Inside the class must be available container по которому можно итерироваться.
# После определения методов __iter__ and __next__ - гараж начал итерироваться по своим машинам.

import random
import uuid
import pprint

models = ("Skoda", "Lada", "Toyota", "Ford", "Lexus")
towns = ("Rome", "Kiev", "Riga", "Boston", "London")

class Car:
    def __init__(self, number, model, year):
        self.number = number
        self.model = model
        self.year = year

cars = []
for i in range(20):
    cars.append(Car(uuid.uuid4(), random.choice(models), random.randrange(1980, 2018)))

# pprint.pprint(cars)




class Garage:
    def __init__(self, number, town, places):
        self.number = number
        self.town =  town
        self.places = places
        self.cars = cars if cars is not None else []
        self.current = 0   # start index for iteration


    def __iter__(self):
            return self

    def __next__(self):
        if self.current < len(self.cars):
            res = self.cars[self.current]
            self.current += 1
            return res
        else:
            self.current = 0                # Обнуляем индекс
            raise StopIteration             # вызываем остановку итерации




my_garage = Garage(uuid.uuid4(), random.choice(towns), 20)
my_garage.cars = cars
# print(my_garage.number)

for car in my_garage:
    print(car)