from __future__ import annotations
import random
import uuid
import constants
import json


class Car:
    def __init__(self, price:float, mileage:float):
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
    #
    # @staticmethod
    # def to_json(obj: Car):
    #     data = {"price": obj.price,
    #             "type": obj.type,
    #             "producer": obj.producer,
    #             "number": obj.number,
    #             "mileage": obj.mileage}
    #     return data
    #
    # @classmethod
    # def from_json(cls, data):
    #     price = data["price"]     # обязательные параметры, кот. вводятся при создании объекта
    #     mileage = data["mileage"]  # обязательный объект, кот. вводится при создании объекта.
    #     car_instance = Car(price, mileage) # воссоздание экземпляра класса по обязательным атрибутам
    #     car_instance.type = data.get("type", random.choice(constants.CARS_TYPES)) # прописываем необязат. атрибуты
    #     car_instance.producer = data.get("producer", random.choice(constants.CARS_PRODUCER))
    #     car_instance.number = data.get("number", str(uuid.uuid4()))
    #     return car_instance

def to_json(obj: Car):
    data = {"price": obj.price,
            "type": obj.type,
            "producer": obj.producer,
            "number": obj.number,
            "mileage": obj.mileage}
    return data

def from_json(data):
    price = data["price"]  # обязательные параметры, кот. вводятся при создании объекта
    mileage = data["mileage"]  # обязательный объект, кот. вводится при создании объекта.
    car_instance = Car(price, mileage) # воссоздание экземпляра класса по обязательным атрибутам
    car_instance.type = data.get("type", random.choice(constants.CARS_TYPES)) # прописываем необязат. атрибуты
    car_instance.producer = data.get("producer", random.choice(constants.CARS_PRODUCER))
    car_instance.number = data.get("number", str(uuid.uuid4()))
    return car_instance




#========================================================================


car1 = Car(34000, 100000)
car2 = Car(60000, 25)
print(car1)
print(car2)

str_car1 = json.dumps(car1, default=to_json)
print(f"str_car1: {str_car1}")
print(type(str_car1))

print("Restore without Hook")
restored_car1 = json.loads(str_car1)
print(type(restored_car1))

separator = "+" * 25 + "\n" * 2 + "+" * 25
print(separator)
print("Restore car1 with hook")
restore_car1_hook = json.loads(str_car1, object_hook=from_json)
print(type(restore_car1_hook))
print(restore_car1_hook)
