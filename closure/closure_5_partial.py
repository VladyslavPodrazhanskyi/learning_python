from functools import partial


def power(exp, base):
    return base ** exp


square = partial(power, 2)
print(square(10))
