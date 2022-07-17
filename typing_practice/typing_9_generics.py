"""
https://medium.com/@steveYeah/using-generics-in-python-99010e5056eb

TypeVar factory, giving the name of the type we want to create
and then capturing that in a variable named T
"""

from typing import Any, List, TypeVar, Dict

T = TypeVar('T')

# T = TypeVar("T", str, int) # T can only represent types of int and str
# T = TypeVar("T", bound=int) # T can only be an int or subtype of int

K = TypeVar('K')
V = TypeVar('V')


def first(container: List[T]) -> T:
    return container[0]


# def fake_first(container: List[T]) -> T:  # error: Incompatible return value type (got "str", expected "T")
#     print(container)
#     return 'a'


def get_item(key: K, container: Dict[K, V]) -> V:
    return container[key]


if __name__ == '__main__':
    list_one = ['a', 'b', 'c']
    print(first(list_one))

    list_two = [1, 2, 3]
    print(first(list_two))

    test: Dict[str, int] = {"k": 1}
    print(get_item("k", test))
