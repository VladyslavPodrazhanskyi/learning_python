#!/usr/bin/python

# types of data in python:

# immutable:
# str:
custom_str = 'skfjswksfjksfsnf'
print(dir(custom_str))
print(custom_str + custom_str)
print(custom_str[2:9:3])  # f, w, f

# int:
some_int = 45
print(dir(some_int))
# print(custom_str + some_int)
# float
some_float = 45.93
print(some_int + some_float)
# boolean False or True
false = False
true = True
# None:
none = None
# tuple
tuple1 = (34, 'sfkskf')
tuple2 = (34,)

# mutable:
# list:
some_list = [234, 34.12, False, None, tuple2, some_float]
some_list[2] = True
list_comprehension = [x**2 for x in range(3, 11)]
print(list_comprehension)

# dict:
some_dict = {'key1': 4, 'key2': 56}
print(some_dict['key1'], some_dict.get('key1'))
some_dict['key3'] = 100
# set:
some_set = {'skf', 1, 'skf'}
print(some_set)


def some_function(*args, **kwargs):
    return (args, kwargs)


print(some_function(3, 4, 'skfjsf', 45, a=6, c='sf'))

some_lambda = lambda x, y: (x + y) / 2

print(some_lambda(15, 25))

print(list(filter(lambda x: not isinstance(x, int), some_list)))


def if_not_int(x):
    return not isinstance(x, int)