def fib_rec(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib_rec(n - 1) + fib_rec(n - 2)


def fib_loop(n):
    fib1 = 1
    fib2 = 1
    i = 0
    while i < n - 2:
        fib_sum = fib1 + fib2
        fib1 = fib2
        fib2 = fib_sum
        i += 1
    return fib2


for i in range(1, 10):
    print((fib_rec(i), fib_loop(i)))