"""
https://docs.python.org/3/howto/descriptor.html#properties

"""
import logging

logging.basicConfig(level=logging.INFO)


class LoggedAgeAccess:

    def __get__(self, obj, objtype=None):
        value = obj._age
        logging.info('Accessing %r giving %r', 'age', value)
        return value

    def __set__(self, obj, value):
        logging.info('Updating %r to %r', 'age', value)
        obj._age = value


class Person:
    age = LoggedAgeAccess()  # Descriptor instance

    def __init__(self, name, age, sex):
        self.name = name  # Regular instance attribute
        self.age = age  # Calls __set__()
        self.sex = sex

    def birthday(self):
        self.age += 1
        # Calls both __get__() and __set__()
        # self.age(set) = self.age(get) + 1


mary = Person('Mary M', 30, 'F')
mary.birthday()
print(vars(mary))
print(mary.__dict__)
print(mary.age)


