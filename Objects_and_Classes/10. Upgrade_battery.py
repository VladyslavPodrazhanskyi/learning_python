# Обновление аккумулятора:
# Добавьте в класс Battery метод с именем upgrade_battery().
# Этот метод должен проверять размер аккумулятора и устанавливать мощность равной 85,
# если она имеет другое значение. Создайте экземпляр электромобиля с аккумулятором
# по умолчанию, вызовите get_range(), а затем вызовите get_range() во второй раз после
# вызова upgrade_battery(). Убедитесь в том, что запас хода увеличился.

class Battery():
    def __init__(self, power=70):
        self.power = power
    def display_power(self):
        print("Power of this battery is " + str(self.power) + " KWH.")
    def get_range(self):
        elcar_range = self.power*4
        return "This car can go {} km.".format(str(elcar_range))
    def upgrade_battery(self):
        if self.power < 85:
            self.power = 85

bat1 = Battery()

bat1.display_power()

print(bat1.get_range())

bat1.upgrade_battery()

print(bat1.get_range())