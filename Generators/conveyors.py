import collections.abc


def gen_range(n: int) -> collections.Iterator:
    i = 1
    while i < n:
        yield i
        i += 1


for i in gen_range(10):
    print("i: {i}".format(i=i))


def natural_num() -> collections.Iterator:
    i = 1
    while True:
        yield i
        i += 1


nat = natural_num()

print(next(nat))
print(next(nat))
print(next(nat))
print(next(nat))

evens_below_twenty = ( x for x in range(20) if x % 2 == 0)


for i in evens_below_twenty:
    print(i)

# conveyors for data processing:

data = natural_num()
evens = (x for x in data if x % 2 == 0)
even_squares = (x ** 2 for x in evens)
even_squares_ending_in_six = (x for x in even_squares if x % 10 == 6)
