import random
from typing import List


def process(a):
    return a ** 2 + 4

def loop_func() -> List[int]:

    data = []

    for i in range(5):
        data.append(process(i))

    return data

if __name__ == '__main__':
    print(loop_func())


