"""
https://mypy.readthedocs.io/en/stable/generics.html

"""
from typing import TypeVar, Generic, List

T = TypeVar('T')


class Stack(Generic[T]):
    def __init__(self) -> None:
        self.items: List[T] = []

    def push(self, item: T) -> None:
        self.items.append(item)

    def pop(self) -> T:
        return self.items.pop()

    def is_empty(self) -> bool:
        return not self.items


if __name__ == '__main__':
    stack1 = Stack[int]()
    stack1.push(3)
    print(stack1.is_empty())
    stack1.pop()
    print(stack1.is_empty())
