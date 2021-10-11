from math import pi


def simple_decor(fn):
    def wrapper():
        res = 15
        res += fn()
        res *= 40
        return res
    return wrapper

# my_func = simple_decor(my_func)


@simple_decor
def square_pi():
    return pi**2


print(square_pi())
