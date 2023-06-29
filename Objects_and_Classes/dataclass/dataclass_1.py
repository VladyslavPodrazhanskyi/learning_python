from dataclasses import dataclass


@dataclass
class Car:
    color: str
    mileage: float
    automatic: bool


for el in dir(Car):
    print(el)

car1 = Car('red', 23535.45, True)


print(car1)  # __repr__ method created automatically
# Car(color='red', mileage=23535.45, automatic=True)

car1.model = 'Mercedes'  # additional field can be added but it will not be added to __repr__ method

print(car1.model)
print(dir(car1))
