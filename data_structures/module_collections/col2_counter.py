"""
collections.Counter: Multisets

The collections.Counter class in the Python standard library implements
a multiset, or bag,
type that allows elements in the set to have more than one occurrence.

This is useful if you need to keep track of not only
if an element is part of a set, but also how many times
it’s included in the set
"""


from collections import Counter, defaultdict


inventory = Counter()
goods = {"apple": 5, "beer": 12}
inventory.update(goods)

print(inventory)  # Counter({'beer': 12, 'apple': 5})

new_goods = {"pear": 7, "beer": 4}
inventory.update(new_goods)
inventory.update(['beer', 'beer', 'apple'])

print(inventory)  # Counter({'beer': 18, 'pear': 7, 'apple': 6})
print(len(inventory))  # 3
print(sum(inventory.values()))  # 31

#########################
words = ['spam', 'egg', 'spam', 'counter', 'counter', 'counter']


dict_counter = {}
defaultdict_counter = defaultdict(int)
col_counter = Counter()

for word in words:
    dict_counter[word] = dict_counter.get(word, 0) + 1
    defaultdict_counter[word] += 1
    col_counter[word] += 1

word_counts = Counter(words)
print(word_counts)  # Counter({'counter': 3, 'spam': 2, 'egg': 1})

# {'spam': 2, 'egg': 1, 'counter': 3}
print(dict_counter)
print(dict(defaultdict_counter))
print(dict(col_counter))

print(col_counter)  # Counter({'counter': 3, 'spam': 2, 'egg': 1})
print(list(col_counter.elements()))  # ['spam', 'spam', 'egg', 'counter', 'counter', 'counter']
print(col_counter.most_common()) # [('counter', 3), ('spam', 2), ('egg', 1)]
print(col_counter.most_common(2)) # [('counter', 3), ('spam', 2)]
#
#
c = Counter(a=4, b=3, c=5, d=-12)
d = Counter(a=5, b=-3, c=9, d=16)

print(c | d)  # max Counter({'d': 16, 'c': 9, 'a': 5, 'b': 3})
# only positive result
print(c + d)  # Counter({'c': 14, 'a': 9, 'd': 4})
print(c - d)  # Counter({'b': 6})

