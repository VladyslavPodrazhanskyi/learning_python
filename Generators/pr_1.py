from sys import getsizeof

gen_range = (i**2 for i in range(1, 20))

print(next(gen_range))

for each in gen_range:
    print(each)


# print(next(gen_range))
print(getsizeof(gen_range))


def gen_without_loop():
    yield 7
    yield 123
    yield 7
    yield 5
    yield 16
    yield 7


my_gen = gen_without_loop()
for each in my_gen:
    print(each)


