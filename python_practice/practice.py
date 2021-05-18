data = (12, 34, 'kjf', 56, 7889.980)

some_dict = dict.fromkeys(data, 45)

print(some_dict)
some_dict.setdefault('new_key')
print(some_dict)
some_dict.setdefault(12, 75)
print(tuple(map(list, some_dict.items())))
# print(some_dict)