# Значение атрибута можно изменить одним из трех способов:
# 1)изменить его прямо  в экземпляре -  редко используется на практике.
# 2) задать значение при помощи метода
# 3) изменить его с приращением.то есть прибавлением определенной величины) при помощи метода.

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



my_car = Car("audi", "a4", 2015)
print(my_car.get_descriptive_name())
my_car.read_odometer()
my_car.odometer_reading = 10000   # изменение значения поля по умолчанию прямо в экземпляре.
my_car.read_odometer()
my_car.update_odometer(11000)     # изменение значения поля с помощью метода
my_car.increment_odometer(100)    # изменение значения поля с помощью метода с приращением
my_car.read_odometer()