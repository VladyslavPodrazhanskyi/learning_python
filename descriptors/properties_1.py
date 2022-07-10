"""
https://www.programiz.com/python-programming/property
"""


class Celsius:
    def __init__(self, temperature=0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32


human = Celsius()
human.temperature = 37

print(human.__dict__)  # {'temperature': 37}
print(vars(human))  # {'temperature': 37}
print(dir(human))  # ['temperature', 'to_fahrenheit'....]

print(human.temperature)  # look at __dict__  (human.__dict__['temperature'])
print(human.to_fahrenheit())
