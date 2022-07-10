"""
https://www.programiz.com/python-programming/property

extend the usability of the Celsius class defined above.
We know that the temperature of any object cannot reach
below -273.15 degrees Celsius (Absolute Zero in Thermodynamics)

However, the bigger problem with the above update is that all the programs
that implemented our previous class have to modify their code
from obj.temperature to obj.get_temperature()
and all expressions like obj.temperature = val to obj.set_temperature(val).

This refactoring can cause problems while dealing
with hundreds of thousands of lines of codes.

All in all, our new update was not backwards compatible.
This is where @property comes to rescue.

"""


class Celsius:
    def __init__(self, temperature=0):
        self.set_temperature(temperature)

    def to_fahrenheit(self):
        return (self.get_temperature() * 1.8) + 32

    # getter method
    def get_temperature(self):
        return self._temperature

    def set_temperature(self, value):
        if value < -273.15:
            raise ValueError('Temperature below -273.15 is not possible.')
        self._temperature = value


human = Celsius(37)
print(human.get_temperature())
print(human.to_fahrenheit())

try:
    human.set_temperature(36.6)
except ValueError as error:
    print(error)

print(human.to_fahrenheit())

# The private variables don't actually exist in Python.
# There are simply norms to be followed. The language itself doesn't apply
# any restrictions.
human._temperature = -300
print(human._temperature)
print(human.__dict__)

# print(human.__dict__)
# print(vars(human))
# print(dir(human))
