import random
from typing import List


def loop_func() -> List[int]:

    x = 5 * random.choice([-1, 1])
    data = []

    while 0 < x < 25:
        res = x ** 2
        data.append(res)
        x = res

    return data

if __name__ == '__main__':
    for _ in range(5):
        print(loop_func())


