"""
https://mypy.readthedocs.io/en/stable/generics.html

"""

from typing import Any, List, TypeVar, Dict, Generic

T = TypeVar('T')


class Box(Generic[T]):
    def __init__(self, content: T) -> None:
        self.content = content


if __name__ == '__main__':
    box1 = Box[int](50)
    box2 = Box(50)              # auto infer
    box3 = Box('some string')   # auto infer
    # box4 = Box[int]('some string')   # error: Argument 1 to "Box" has incompatible type "str"; expected "int"


