from functools import partial


def some_func(
    a: int,
    b: int,
    c: int,
    x: int
) -> int:
    return a ** 3 + b ** 2 + c + x


part_some_func1 = partial(some_func, b=2, c=1, x=15)
part_some_func2 = partial(some_func, 2, 1, 15)
print(part_some_func1(2))
print(part_some_func2(2))



