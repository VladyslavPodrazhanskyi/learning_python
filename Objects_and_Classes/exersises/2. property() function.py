class Person:
    def __init__(self, name="Guest"):
        self.__name = name

    def set_name(self, name):          # assigns the value to the __name attribute.
       self.__name = name

    def get_name(self):                # returns the value of the private instance attribute __name
       return self.__name

p1 = Person('Kolya')
p1.set_name('Vasya')
print(p1.get_name())
print(p1.mro)
