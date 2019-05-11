import random
import uuid
import constants

class Car:
    def __init__(self, price:float, mileage:float ):
        self.price = price
        self.type = random.choice(constants.CARS_TYPES)
        self.producer = random.choice(constants.CARS_PRODUCER)
        self.number = str(uuid.uuid4())
        self.mileage = mileage


    # Автомобілі можна перівнювати між собою за ціною.
    def __eq__(self, other):
        return self.price == other.price
    def __lt__(self, other):
        return self.price < other.price
    def __gt__(self, other):
        return self.price > other.price

    # При виводі(logs, print) автомобілю повинні зазначатися всі його атрибути
    def __str__(self):
        return f"This car: {self.price} USD, {self.type}, {self.producer}, {self.number}, {self.mileage} km."

    #Автомобіль має метод заміни номеру. Номер повинен відповідати UUID
    def change_num(self):
        self.number = str(uuid.uuid4())

car1 = Car(34000, 100000)
car2 = Car(60000, 25)
print(car1)
print(car2)