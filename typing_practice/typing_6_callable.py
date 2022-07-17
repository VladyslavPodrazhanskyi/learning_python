"""
https://realpython.com/python-type-checking/#playing-with-python-types-part-2

https://dbader.org/blog/python-first-class-functions

Python’s functions are first-class objects.
You can assign them to variables, store them in data structures,
pass them as arguments to other functions,
and even return them as values from other functions.

 That also means that you need to be able to add type hints representing functions.

typing.Callable represents:
Functions,
lambdas,
methods
classes

https://mypy.readthedocs.io/en/latest/cheat_sheet_py3.html

"""
from typing import Callable


def do_twice(func: Callable[[str], str], argument: str) -> None:
    print(func(argument))
    print(func(argument))


def create_greeting(name: str) -> str:
    return f'Hello, {name}!'


do_twice(create_greeting, 'Vlad')
