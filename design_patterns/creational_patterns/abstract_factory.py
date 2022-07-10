class Dog:
    def __init__(self, name: str) -> None:
        self._name = name

    def speak(self) -> str:
        return 'Woof!'

    def __str__(self):
        return 'Dog'


class DogFactory:
    """Concrete factory"""

    def get_pet(self):
        """Returns a dog object"""
        return Dog('Defalt_name')

    def get_food(self):
        """Returns a dog food object"""
        return 'Dog food!'


class PetStore:
    """ PetStore houses our Abstract factory """
    def __init__(self, pet_factory=None):
        """ pet_factory is our Abstract Factory """

        self._pet_factory = pet_factory

    def show_pet(self) -> None:
        """ Utility method to display the details of the returned objects """
        pet = self._pet_factory.get_pet()
        pet_food = self._pet_factory.get_food()

        print('Our pet is {}!'.format(pet))
        print('Our pet says hello by {}!'.format(pet.speak()))
        print("It's food is {}".format(pet_food))


# Create a concrete factory
factory = DogFactory()
# Create a pet store housing our Abstract Factory
shop = PetStore(factory)
# Invoke the utiltiy method to show the details of our pet
shop.show_pet()