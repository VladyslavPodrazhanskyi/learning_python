from collections import namedtuple


Car = namedtuple("Car", "color mileage") # == namedtuple("Car", ["color", "mileage"])

my_car = Car("red", 345.2)

print(my_car.color)
print(my_car.mileage)
