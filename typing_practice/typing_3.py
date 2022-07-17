"""
https://realpython.com/python-type-checking/#example-a-deck-of-cards

The answer hides behind the academic sounding term structural subtyping.
 One way to categorize type systems is by whether they are nominal or structural:

In a nominal system, comparisons between types are based on names and declarations.
The Python type system is mostly nominal,
where an int can be used in place of a float because of their subtype relationship.

In a structural system, comparisons between types are based on structure.
 You could define a structural type Sized that includes all instances that define .__len__(), irrespective of their nominal type.

A protocol specifies one or more methods that must be implemented. For example,
all classes defining .__len__() fulfill the typing.Sized protocol

Other examples of protocols defined in the typing module include
Container,
Iterable,
Awaitable,
ContextManager.
"""
from typing import Sized


def len(obj: Sized):
    return obj.__len__()


"""
A common pattern in Python is to use None as a default value for an argument. 
This is usually done either to avoid problems with mutable default values or 
to have a sentinel value flagging special behavior
"""

