from typing import List


def list_sum(data: List) -> int:
    if not data:
        return 0
    return data[0] + list_sum(data[1:])


print(list_sum([1, 0, 34, 23, -11]))


