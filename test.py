from pprint import pprint
# i = int('45')
# print('i', '__hash__' in dir(i))
# f = 56.09
# print(f, f.__hash__(), sep=':::')
# print('f', '__hash__' in dir(f))
#
s = 'sdjhfskdjhfk'
# print(s, s.__hash__(), sep=':::')
# print('s', '__hash__' in dir(s))
# t = 'sjfhd', 435, 'ksjf'
# print(t, t.__hash__(), sep=':::')
# print('t', '__hash__' in dir(t))
# l = list(range(0, 23, 4))
# l.extend(['sjfhd', 435, 'ksjf'])
# print('l', '__hash__' in dir(l))



l = [x**3 for x in range(-5, 25) if x % 2 == 1]

print(l, type(l))
print('hash_check', '__hash__' in dir(l))
print('next_check', '__next__' in dir(l))
pprint(dir(l))
print(id(l))
print(id(s), s.__hash__(), sep='^^^')


gen = iter(l)
print('hash_check', '__hash__' in dir(gen))
print('next_check', '__next__' in dir(gen))
print(gen.__hash__())

# r = range(50)
# print(r.__hash__())
# print('next_check', '__next__' in dir(r))
# gr = iter(r)
# print(gr.__hash__())
# print('next_check', '__next__' in dir(gr))

t1 = (1, 'skfhdskf', 'sfhdsjfh')
t2 = (1, 'yutyu', 'sfhdsjfh')
print('t1', t1.__hash__())
print('t2', t2.__hash__())

l2 = list(range(11))
l2 += [11]
print(l2)

l3 = list(range(11))
l3.append(11)
print(l3)

print(l2 == l3)