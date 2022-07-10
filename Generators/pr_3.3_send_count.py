from time import sleep


def count_gen(start=0, step=1, stop=10):
    n = start
    while n < stop:
        val = yield n
        if val is not None:
            n = val
        n += step


print('cg_10')

cg_10 = count_gen()
for item in cg_10:
    print(item)

# print(next(cg_10))  # StopIteration

cg_20 = count_gen(stop=20)

print('cg_20')
for item in cg_20:
    sleep(2)
    print(item)
    if item > 3:
        print(cg_20.send(18))

# print(next(cg_20))