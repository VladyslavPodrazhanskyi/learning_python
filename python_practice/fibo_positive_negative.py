def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n > 1:
        return fibo(n - 1) + fibo(n - 2)
    else:
        return fibo(n + 2) - fibo(n + 1)


data = range(-10, 11)

for el in data:
    print(fibo(el), end=' ')

