"""
https://pythonist.ru/slozhnoe-uporyadochivanie/
"""

from typing import List


def make_grlex(words_list: List[str]) -> List[str]:
    return sorted(words_list, key=lambda x: (len(x), x)) # first by len, then by alpha(default sort)
    # return sorted(sorted(words_list), key=lambda x: len(x))   # ????


assert make_grlex(["small", "big"]) == ["big", "small"]
assert make_grlex(["cat", "ran", "for", "the", "rat"]) == ["cat", "for", "ran", "rat", "the"]
assert make_grlex(["this", "is", "a", "small", "test"]) == ["a", "is", "test", "this", "small"]
