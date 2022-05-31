from collections import Counter, defaultdict


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
