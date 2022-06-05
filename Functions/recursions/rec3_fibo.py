from typing import List


def fibo_numbers(num: int) -> int:
    if num < 2:
        return num
    return fibo_numbers(num - 2) + fibo_numbers(num - 1)


for i in range(10):
    print(fibo_numbers(i))