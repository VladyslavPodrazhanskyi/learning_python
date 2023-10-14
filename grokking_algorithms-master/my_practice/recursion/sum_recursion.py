from typing import List


def recur_sum(arr: List[int]) -> int:
    if len(arr) == 0:
        return 0
    return arr[0] + sum(arr[1:])


def loop_sum(arr: List[int]) -> int:
    sum = 0
    for el in arr:
        sum += el
    return sum


if __name__ == '__main__':
    print(recur_sum([2, 5, -2, 11]))
    print(loop_sum([2, 5, -2, 11]))
