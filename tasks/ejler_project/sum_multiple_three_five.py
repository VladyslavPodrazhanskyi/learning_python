"""
https://pythonist.ru/zadacha-1-proekt-ejlera/
"""


def sum_multiple_three_five() -> int:
    return sum([i for i in range(1000) if (i % 3 == 0 or i % 5 == 0)])


print(sum_multiple_three_five())
