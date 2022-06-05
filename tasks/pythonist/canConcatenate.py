"""
https://pythonist.ru/sliyanie-spiskov/
"""

from typing import List


def can_concatenate(lst: List[List[int]], target: List[int]) -> bool:
    # sum_list = lst[0]
    # for lst_el in lst[1:]:
    #     sum_list += lst_el
    # return sorted(sum_list) == sorted(target)
    return sorted(sum(lst, [])) == sorted(target)


assert can_concatenate([[1, 2, 3, 4], [5, 6], [7]], [1, 2, 3, 4, 5, 6, 7])
assert can_concatenate([[2, 1, 3], [5, 4, 7, 6]], [7, 6, 5, 4, 3, 2, 1])
assert not can_concatenate([[2, 1, 3], [5, 4, 7, 6, 7]], [1, 2, 3, 4, 5, 6, 7])
assert not can_concatenate([[2, 1, 3], [5, 4, 7]], [1, 2, 3, 4, 5, 6, 7])

