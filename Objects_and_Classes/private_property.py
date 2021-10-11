from sys import getsizeof

class Dog:
    def __init__(self, petname):
        self.__petname = petname

    @property
    def petname(self):
        return self.__petname

    @petname.setter
    def petname(self, value):
        self.__petname = value

    @petname.deleter
    def petname(self):
        del self.__petname


class Poodle(Dog):
    print(locals())



d1 = Dog('Barbos')

# print(d1._Dog__petname)
print(d1.petname)
d1.petname = 'Tobik'
print(d1.petname)
del d1.petname
# print(d1.petname)
d1.petname = 'Igor'
print(d1.petname)
#
# p1 = Poodle()
# p2 = Poodle()
#
# print(getsizeof(Poodle))
# print(getsizeof(p1))
# print(getsizeof(p2))
