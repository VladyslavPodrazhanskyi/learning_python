"""
https://pythonist.ru/bigrammy/
"""

from typing import List


def can_find(bigrams: List[str], words: List[str]) -> bool:
    return all(any(b in w for w in words) for b in bigrams)
    # for b in bigrams:
    #     if not any(b in w for w in words):
    #         return False
    # return True


assert can_find(["at", "be", "th", "au"], ["beautiful", "the", "hat"]) == True
assert can_find(["ay", "be", "ta", "cu"], ["maybe", "beta", "abet", "course"]) == False
assert can_find(["th", "fo", "ma", "or"], ["the", "many", "for", "forest"]) == True
assert can_find(["oo", "mi", "ki", "la"], ["milk", "chocolate", "cooks"]) == False