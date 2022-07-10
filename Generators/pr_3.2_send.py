def numberGenerator(n):
    number = yield
    while number < n:
        number = yield number
        number += 1


g = numberGenerator(10)    # Create our generator
print(next(g))
print(g.send(5))
print(g.send(5))
print(g.send(8))