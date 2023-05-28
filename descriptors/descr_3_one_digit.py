class OneDigitNumericValue():
    def __init__(self, name):
        self.name = name

    def __get__(self, obj, type=None) -> object:
        return obj.__dict__.get(self.name) or 0

    def __set__(self, obj, value) -> None:
        if isinstance(value, int) and 0 <= value < 10:
            obj.__dict__[self.name] = value
        else:
            raise ValueError('value shoud be 1 digit int')


class Foo():
    number = OneDigitNumericValue('Max')


my_foo_object = Foo()
my_second_foo_object = Foo()

my_foo_object.number = 3
print(my_foo_object.number)
my_foo_object.number = 1
print(my_foo_object.number)
print(my_second_foo_object.number)

my_third_foo_object = Foo()
print(my_third_foo_object.number)
