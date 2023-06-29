"""
Using namedtuple objects over regular (unstructured) tuples and dicts
can also make your coworkers’ lives easier by making the data
that’s being passed around
self-documenting
"""

from collections import namedtuple

Car = namedtuple('Car', 'color mileage automatic')

car1 = Car(color='red', mileage=12000, automatic=True)

print(car1.mileage)  # 12000

print(car1)  # Car(color='red', mileage=12000, automatic=True)


"""
 typing.NamedTuple is the younger sibling of the namedtuple class
in the collections module. 
It’s very similar to namedtuple, 
with the main difference being an updated syntax 
for defining new record types and added support for type hints.
"""
from typing import NamedTuple


class Auto(NamedTuple):
    color: str
    mileage: float
    automatic: bool


car2 = Auto('green', 12987, False)

print(car2)          # Auto(color='green', mileage=12987, automatic=False)
print(car2.mileage)  # 12987
