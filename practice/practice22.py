def add(a, b):
    return a + b


def test_add():
    assert (add(1, 2) == 3)
    assert (add(0, 0) == 0)


def fibbonaci_recursion(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibbonaci_recursion(n - 1) + fibbonaci_recursion(n - 2)


# write fibonacci function without recursion
def fibbonaci_iterative(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        result = 1
        prev = 0
        for i in range(1, n):
            temp = result
            result += prev
            prev = temp
        return result
