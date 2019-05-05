# 1) Ассоциация(агрегация, композиция)
# Агрегация -  экземпляр аккумулятор создается где-то в другом месте кода,
# и передается в конструктор автомобиля в качестве параметра.

# Создание отдельного класса Battery (перемещение в него всех атрибутов и методов аккумулятора),
# Превращение экземпляра Battery в атрибут класса ElectricCar
# Обязательная агрегация так как объект класса Battery прописан в коде класса как постоянный атрибут.


class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.read_odometer = 0
    def display_car(self):
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name
    def increment_odometer(self, current_mileage):
        self.read_odometer += current_mileage
    def fill_gas_tank(self):
        print("Tank of your car is full now")

# Test of instance Car.
my_car = Car("Toyota", "Corolla", 2017)
print(my_car.display_car())
my_car.fill_gas_tank()



class Battery():
    def __init__(self, battery_power=70):
        self.battery_power = battery_power
    def describe_battery(self):
        print("This car has battery " + str(self.battery_power) + " KWH power.")
    def get_range(self):
        range = self.battery_power*4
        print("You can go about " + str(range) + " km.")

bat1 = Battery()
bat1.describe_battery()
bat2 = Battery(150)
bat2.describe_battery()

# Экземпляр класса Battery является необязательным атрибутом при создании экземпляра ( есть значение по умолчанию).
class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery(70)       # помещаем экземпляр класса battery как атрибут класса ElectricCar

my_tesla = ElectricCar("Tesla", "A4", 2018)

my_tesla.battery.describe_battery()   # вызов метода класса battery из экземпляра класс ElectricCar.
my_tesla.battery.get_range()

