"""
A set is an unordered collection of objects
that doesn’t allow duplicate elements.
Typically, sets are used to quickly test a value for membership
 in the set,
 to insert or delete new values from a set,
 and to compute the union or intersection of two sets.

 membership tests are expected to run in fast O(1) time

Union, intersection, difference, and subset operations
should take O(n) time on average.

Any hashable object can be stored in a set

If you need hashable objects that can be used as dictionary or set keys,
then use a frozenset
"""
from utils import is_hashable

set_vowels = {"a", "e", "i", "o", "u"}
print(is_hashable(set_vowels))  # False
frozen_vowels = frozenset(set_vowels)
print(is_hashable(frozen_vowels))  # True


