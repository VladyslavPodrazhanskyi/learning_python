from typing import Dict
from datetime import datetime
from functools import lru_cache

memo: Dict[int, int] = {0: 0, 1: 1}


# def fibo(n):
#     if n not in memo:
#         memo[n] = fibo(n - 1) + fibo(n - 2)
#     return memo[n]


# @lru_cache(maxsize=None)
# def fibo(n):
#     if n < 2:
#         return n
#     return fibo(n - 1) + fibo(n - 2)



def fibo(n):
    prev, cur = 0, 1
    for i in range(n):
        prev, cur = cur, prev + cur
    return prev


def main():
    start = datetime.now()
    print(fibo(7))
    finish = datetime.now()
    print(finish - start)


if __name__ == '__main__':
    main()
