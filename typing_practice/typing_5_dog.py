"""
https://realpython.com/python-type-checking/#playing-with-python-types-part-2



"""


# dogs.py

from datetime import date
from typing import TypeVar, Type

# The type variable TAnimal is used to denote
# that return values might be instances of subclasses of Animal.
# We specify that Animal is an upper bound for TAnimal.
# Specifying bound means that TAnimal will only be Animal or one of its subclasses.
# This is needed to properly restrict the types that are allowed.

TAnimal = TypeVar("TAnimal", bound="Animal")


class Animal:
    def __init__(self, name: str, birthday: date) -> None:
        self.name = name
        self.birthday = birthday

    # The typing.Type[] construct is the typing equivalent of type().
    # You need it to note that the class method expects a class
    # and returns an instance of that class.

    @classmethod
    def newborn(cls: Type[TAnimal], name: str) -> TAnimal:
        return cls(name, date.today())

    def twin(self: TAnimal, name: str) -> TAnimal:
        cls = self.__class__
        return cls(name, self.birthday)


class Dog(Animal):
    def bark(self) -> None:
        print(f"{self.name} says woof!")


fido = Dog.newborn("Fido")
pluto = fido.twin("Pluto")
fido.bark()
pluto.bark()



