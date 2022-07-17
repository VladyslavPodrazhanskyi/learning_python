"""
https://www.programiz.com/python-programming/property

"""
# using property decorator
class Celsius:
    def __init__(self, temperature=0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    # getter
    @property
    def temperature(self):
        print('Getting value ...')
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        print('Setting value ...')
        if value < -237.15:
            raise ValueError("Temperature below -273.15 is not possible")
        self._temperature = value


human = Celsius(37)  # calling setter
print(human.temperature)
print(human.to_fahrenheit())
human.temperature = -300
# call descriptor which validate value instead of __dict__ look up

print(human.__dict__)  # {'_temperature': 37}
print(vars(human))  # {'_temperature': 37}
print(dir(human))  # ['_temperature', 'get_temperature', 'set_temperature', 'temperature', 'to_fahrenheit' ...]
