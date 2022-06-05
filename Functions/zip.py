list1 = ['a', 'b', 'c']
list2 = ['x', 'y', 'z', 'w']

# [('a', 'x'), ('b', 'y'), ('c', 'z')]
zipped1 = [(x, y) for x, y in zip(list1, list2)]
zipped2 = [pair for pair in zip(list1, list2)]

# separate dif pair
pair1, pair2, pair3 = zipped1
print(pair1)   # ('a', 'x')
print(pair2)   # ('b', 'y')
print(pair3)   # ('c', 'z'

# unzip
first_pair_members, second_pair_members = zip(*zipped1)
print(first_pair_members)  # ('a', 'b', 'c')
print(second_pair_members) # ('x', 'y', 'z')


# unpack args:

def summator(a: int, b: int) -> int:
    return a + b


data = [5, 4]

try:
    print(summator(data))
except TypeError:
    print('summator expects 2 int args')

try:
    print(summator(*data))
except TypeError:
    print('summator expects 2 int args')