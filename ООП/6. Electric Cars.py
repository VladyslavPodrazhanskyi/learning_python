# 1)Работа над новым классом не обязана начинаться с нуля. Если класс, который вы
# пишете, представляет собой специализированную версию ранее написанного клас-
# са, вы можете воспользоваться наследованием. Один класс, наследующий от другого,
# автоматически получает все атрибуты и методы первого класса. Исходный класс
# называется родителем, а новый класс — потомком. Класс-потомок наследует
# атрибуты и методы родителя, но при этом также может определять собственные
# атрибуты и методы.

# 2)Переопределение (OVERRIDE)метода fill_gas_tank из родительского класса Car, в наслднике ElectricCar.


# Parent class
class Car():
    def __init__(self, make, model, year):
        self.make =  make
        self.model = model
        self.year = year
        self.odometer_reading = 0               # поле экз. класса со значением по умолчанию.
    def get_descriptive_name(self):
        long_name = str(self.year), self.make.title(), self.model.title()
        return long_name
    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")
    def update_odometer(self, mileage):              # изменение поля экз. класс с помощью метода
        """
        Устанавливает на одометре заданное значение.
        При попытке обратной подкрутки изменение отклоняется.

        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, additional_mileage):
        if additional_mileage >= 0:
            self.odometer_reading += additional_mileage
        else:
            print("You can't roll back an odometer!")
    def fill_gas_tank(self):
        print("Gas tank of this car is full.")

used_car = Car("Skoda", "Oktavia", 2001)
used_car.fill_gas_tank()

# Child class
class ElectricCar(Car):
    def __init__(self, make, model, year):  # метод __init__ получает инф-цию, необхд. для созд. экземпляра род. класса.
# Функция super() в строке  — специальная функция, которая помогает Python связать потомка с родителем.
# Эта строка приказывает Python вызвать метод  __init__() класса, являющегося родителем ElectricCar ,
# в результате чего экземпляр ElectricCar получает все атрибуты класса-родителя
        super().__init__(make, model, year)

# Определение атрибутов и методов для класса-потомка:
        self.battery_power  = 70
    def display_battery_power(self):
        print("My battery Power is " + str(self.battery_power) + " .")
    def set_battery_power(self, power):
        self.battery_power = power
    def fill_gas_tank(self):                   #   переопределение (override) в классе ElectricCar метода fill_gas_tank
        print("This car doesn't have a gas tank.")




my_tesla = ElectricCar("tesla", "model s", 2016)
print(my_tesla.get_descriptive_name())
my_tesla.display_battery_power()
my_tesla.set_battery_power(128)
my_tesla.display_battery_power()
my_tesla.fill_gas_tank()