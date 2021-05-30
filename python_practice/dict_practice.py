data = (12, 34, 'kjf', 56, 7889.980)
data2 = ('kpsfj', '782378')

some_dict = dict.fromkeys(data)

some_dict.setdefault('new_key')
print(some_dict)

print(tuple(map(list, some_dict.items())))
print(some_dict)

d = {1: "one", 2: "two"}
d1 = {3: "three"}

d.update(d1)
print(d)


d.update(x = 5, y = 3)

print(d)