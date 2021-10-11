from functools import reduce
import operator

data = [1, 2, 3, 45, 11, 34]
alone = [5]
empty = []

print(reduce(lambda x, y: x * y, alone, 1))
# print(reduce(operator.mul, empty))