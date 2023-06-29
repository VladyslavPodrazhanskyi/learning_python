"""
The namedtuple class aprovides an extension of the built-in tuple data type.
Similar to defining a custom class,
using namedtuple allows you to define reusable blueprints for your records
that ensure the correct field names are used.

namedtuple objects are immutable, just like regular tuples.
This means you can’t add new fields
or modify existing fields after the namedtuple instance is created.
"""

from collections import namedtuple
from sys import getsizeof

p1 = namedtuple("Point", "x y z")(1, 2, 3)
p2 = (1, 2, 3)

print(getsizeof(p1))  # 64

print(getsizeof(p2))  # 64

print(f'type p1: {type(p1)}')  # type p1: <class '__main__.Point'>
print(f'p1: {p1}')             # p1: Point(x=1, y=2, z=3)

print(p1.x, p1[0])    # 1 1
print(p1.x is p1[0])  # True
print(p2[0])  # 1
