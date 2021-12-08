from collections import Counter


words = ['spam', 'egg', 'spam', 'counter', 'counter', 'counter']

dict_counter = {}
col_counter = Counter()

for word in words:
    dict_counter[word] = dict_counter.get(word, 0) + 1
    col_counter[word] += 1

print(dict_counter)
print(col_counter)


print(list(col_counter.elements()))
print(col_counter.most_common(2))


c = Counter(a=4, b=3, c=5, d=-12)
d = Counter(a=5, b=-3, c=9, d=16)


print(c | d)
print(c + d)
print(c - d)
