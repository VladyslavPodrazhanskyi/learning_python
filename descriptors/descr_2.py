"""
https://docs.python.org/3/howto/descriptor.html#properties

"""
import logging

logging.basicConfig(level=logging.INFO)


class LoggedAccess:

    def __set_name__(self, owner, name):
        self.public_name = name
        self.private_name = '_' + name

    def __get__(self, obj, objtype=None):
        value = getattr(obj, self.private_name)
        logging.info('Accessing %r giving %r', self.public_name, value)
        return value

    def __set__(self, obj, value):
        logging.info('Updating %r to %r', self.public_name, value)
        setattr(obj, self.private_name, value)


class Person:
    name = LoggedAccess()  # First descriptor instance
    age = LoggedAccess()  # Second descriptor instance

    def __init__(self, name, age):
        self.name = name  # Calls the first descriptor
        self.age = age  # Calls the second descriptor

    def birthday(self):
        self.age += 1


# vars() to look up the descriptor without triggering it

# vars(Person) : {'__module__': '__main__', 'name': <__main__.LoggedAccess object at 0x7f37d20d15e0>, 'age': <__main__.LoggedAccess object at 0x7f37d20d1610>, '__init__': <function Person.__init__ at 0x7f37d1ff7310>, 'birthday': <function Person.birthday at 0x7f37d1ff73a0>, '__dict__': <attribute '__dict__' of 'Person' objects>, '__weakref__': <attribute '__weakref__' of 'Person' objects>, '__doc__': None}

# vars(Person)['name'] # <__main__.LoggedAccess object at 0x7fc79c9c75e0>

print(vars(vars(Person)['name']))  # {'public_name': 'name', 'private_name': '_name'}

pete = Person('Peter', 10)
# INFO:root:Updating 'name' to 'Peter'
# INFO:root:Updating 'age' to 10

print(vars(pete))  # {'_name': 'Peter', '_age': 10}  The two Person instances contain only the private names:
print(dir(pete))  # contain both public and protected attributes.