def fibo_gen(stop):
    a, b = 0, 1
    while b <= stop:
        yield b
        a, b = b, a + b


fib_g = fibo_gen(45)

for i in range(100):
    print(next(fib_g))
