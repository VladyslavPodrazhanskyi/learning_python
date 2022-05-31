from collections import defaultdict


# int

word_count = defaultdict(int)


document = ['sdkfjs', 'sdkfj', 'sdkfsfdjs', 'sdkyyfj', 'sdkfjs', 'sdkfj',]

for word in document:
    word_count[word] += 1

print(dict(word_count))


# list

list_dd = defaultdict(list)

list_dd['list2'].append(45)

print(list_dd)  # defaultdict(<class 'list'>, {'list2': [45]})
print(dict(list_dd))  # {'list2': [45]}

# dict

dict_dd = defaultdict(dict)

dict_dd['outer_key1']['inner_key1'] = 'value11'
dict_dd['outer_key1']['inner_key2'] = 'value12'
dict_dd['outer_key2']['inner_key3'] = 'value23'

print(dict(dict_dd)) # {'outer_key1': {'inner_key1': 'value11', 'inner_key2': 'value12'}, 'outer_key2': {'inner_key3': 'value23'}}

pair_dd = defaultdict(lambda: [0, 0])
pair_dd['outer_key1'][1] = 56
pair_dd['outer_key2'][0] = 44
pair_dd['outer_key2'][1] = 55

print(dict(pair_dd))  # {'outer_key1': [0, 56], 'outer_key2': [44, 55]}

pair_dd['outer_key2'][2] = 55  #IndexError: list assignment index out of range

