from types import MappingProxyType

writable = {'one': 1, 'two': 2}

read_only = MappingProxyType(writable)

writable['three'] = 3

print(read_only)   # {'one': 1, 'two': 2, 'three': 3}
