from sys import getsizeof

some_list = list(range(0, 100_000_000))
print(type(some_list))
print(getsizeof(some_list))

iter_some_list = iter(some_list)
print(type(iter_some_list))
print(getsizeof(iter_some_list))

next(iter_some_list)

for i in range(10):
    print(getsizeof(next(iter_some_list)))

print(next(iter_some_list))

# 1 method for generator
range_gen = (x ** 2 for x in range(10))

for el in range_gen:
    print(el)


# 2 generator function

def iter_gen(start, stop):
    for i in range(start, stop):
        yield i**3


ig = iter_gen(1, 5)

print(next(ig))
print(next(ig))
print(next(ig))
print(next(ig))
print(next(ig))
print(next(ig))
