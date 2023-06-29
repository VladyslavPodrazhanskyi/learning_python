'''
Fields stored on classes are mutable,
and new fields can be added freely, which you may or may not like.
It’s possible to provide more access control and to create read-only fields using the @property decorator,
but once again, this requires writing more glue code.
'''

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
