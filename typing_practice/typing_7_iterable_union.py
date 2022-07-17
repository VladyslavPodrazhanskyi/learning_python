"""

https://mypy.readthedocs.io/en/latest/getting_started.html

# In the above examples, the type signature is perhaps a little too rigid.
# After all, there’s no reason why this function must accept specifically
# a list – it would run just fine if you were to pass in a tuple, a set, or any other custom iterable.
#
# You can express this idea using the collections.abc.Iterable
# (or typing.Iterable in Python 3.8 and earlier) type instead of list :



"""

from collections.abc import Iterable  # or "from typing import Iterable"
from typing import Union


def greet_all(names: Iterable[str]) -> None:
    for name in names:
        print('Hello ' + name)


# As another example, suppose you want to write a function that can accept either ints or strings,
# but no other types. You can express this using the Union type:


def normalize_id(user_id: Union[int, str]) -> str:
    if isinstance(user_id, int):
        return 'user-{}'.format(100000 + user_id)
    else:
        return user_id
