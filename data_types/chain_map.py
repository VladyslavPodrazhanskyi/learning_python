from collections import ChainMap

dict1 = {'dаy1': 'Mоn', 'dаy2': 'Tuе'}
dict2 = {'dаy3': 'Wеd', 'dаy1': 'Thu'}

# if both dict have the same key, first one will be in the result map
res1 = ChainMap(dict1, dict2)
res2 = ChainMap(dict2, dict1)

print(type(res1))
print(res1)

print(res1.maps)        # [{'dаy1': 'Mоn', 'dаy2': 'Tuе'}, {'dаy3': 'Wеd', 'dаy1': 'Thu'}]
print(type(res1.maps))  # list

print('\n', 'res1')
print(list(res1.keys()))
print(list(res1.values()))

print('\n', 'res2')
print(list(res2.keys()))
print(list(res2.values()))

print('elements res1')
for k, v in res1.items():
    print(k, v)
