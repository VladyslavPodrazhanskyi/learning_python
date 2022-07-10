"""
https://www.programiz.com/python-programming/property

Note: The actual temperature value is stored in the
private _temperature variable.
The temperature attribute is a property object
which provides an interface to this private variable.

"""


# using property class
class Celsius:
    def __init__(self, temperature=0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    # getter
    def get_temperature(self):
        print('Getting value ...')
        return self._temperature

    # setter
    def set_temperature(self, value):
        print('Setting value ...')
        if value < -237.15:
            raise ValueError("Temperature below -273.15 is not possible")
        self._temperature = value

    # descriptor - override line nine self.temperature = temperature
    # by calling setter
    temperature = property(get_temperature, set_temperature)


human = Celsius(37)  # calling setter
print(human.temperature)
print(human.to_fahrenheit())
human.temperature = -300
# call descriptor which validate value instead of __dict__ look up

print(human.__dict__)  # {'_temperature': 37}
print(vars(human))     # {'_temperature': 37}
print(dir(human))      # ['_temperature', 'get_temperature', 'set_temperature', 'temperature', 'to_fahrenheit' ...]


