"""
https://pythonist.ru/poslednij-element/
"""

from typing import List


def match_last_item(data: List[str]) -> bool:
    return ''.join(map(str, data[:-1])) == data[-1]
    # return ''.join(str(el) for el in data[:-1]) == data[-1]


assert match_last_item(["rsq", "6hi", "g", "rsq6hig"])
assert match_last_item([8, "thunder", True, "8thunderTrue"])
assert not match_last_item([1, 1, 1, "11"])
