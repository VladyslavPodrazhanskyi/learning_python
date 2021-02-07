# Чтобы к классу можно было применить in для проверки наличия или отсутствие в
# поле-контейнер того или иного элемента, в классе нужно прописать метод
#  __contains__


import uuid
import random

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


    def __contains__(self, item):
        return item in self.cars




my_garage = Garage(uuid.uuid4(), random.choice(towns), 20)
my_garage.cars = cars
# print(my_garage.number)


car1 = cars[5]
car2 = Car(uuid.uuid4(), random.choice(models), random.randrange(1980, 2018))

print(car1 in my_garage)   # True
print(car2 in my_garage)   # False