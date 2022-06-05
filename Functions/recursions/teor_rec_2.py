'''
https://pythonist.ru/rekursivnye-funkczii-v-python/
'''


def recur_fact(n: int) -> int:
    if n in (0, 1):
        return 1
    return n * recur_fact(n - 1)


def iter_fact(n: int):
    res = 1
    if n > 1:
        for i in range(1, n + 1):
            res *= i
    return res


print(recur_fact(8))
print(iter_fact(8))
