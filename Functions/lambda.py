#  Lambda with name
l_func = lambda x, y, z: abs(x) + abs(y) - z
res = l_func(1, -4, -7)
print(res)

# Lambda without name
res = (lambda x, y: (x + y)**2)(3, 1)
print(res)

# Lambda as higher order function with inner lambda as the argument:

higher_order = lambda x, func: x + func(x)
res = higher_order(7, lambda x: x**2)
print(res)

res = (lambda x: (x % 2 and 'odd' or 'even'))(3)
print(res)