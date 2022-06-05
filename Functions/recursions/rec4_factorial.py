from math import factorial

def fact(num: int) -> int:
    if num < 2:
        return 1
    else:
        return num * fact(num - 1)


print(fact(8))
print(factorial(8))
