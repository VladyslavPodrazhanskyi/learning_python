def fibo_gen(stop):
    prev, cur = 0, 1
    while cur <= stop:
        yield cur
        prev, cur = cur, prev + cur

fib_gen = fibo_gen(15)

for el in fib_gen:
    print(el)

print(next(fib_gen))