# dogs.py

from datetime import date


class Animal:
    def __init__(self, name: str, birthday: date) -> None:
        self.name = name
        self.birthday = birthday

    @classmethod
    def newborn(cls, name: str) -> 'Animal':
        return cls(name, date.today())

    def twin(self, name: str) -> 'Animal':
        cls = self.__class__
        return cls(name, self.birthday)


class Dog(Animal):
    def bark(self) -> None:
        print(f"{self.name} says woof!")


fido = Dog.newborn("Fido")
pluto = fido.twin("Pluto")
fido.bark()
pluto.bark()

# mypy error: error: "Animal" has no attribute "bark"
# The issue is that even though the inherited Dog.newborn() and Dog.twin()
# methods will return a Dog the annotation says that they return an Animal.
