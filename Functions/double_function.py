def magic(*args, **kwargs):
    print(args)
    print(kwargs)


magic(1, 2, k1='word1', k2='word2')


def fourth_mult(a, b, c, d):
    return a * b * c * d


list_data = [2, 3]
dict_data = {'c': 4, 'd': 7}


assert fourth_mult(*list_data, **dict_data) == 168


def double(func):
    def g(*args, **kwargs):
        return 2 * func(*args, **kwargs)
    return g


def plus_one(x):
    return x + 1






g1 = double(plus_one)
assert g1(5) == 12   # (5 + 1) * 2
assert g1(-2) == -2  # (-2 + 1) * 2

g2 = double(fourth_mult)

assert(g2(2, 3, 6, 1)) == 72