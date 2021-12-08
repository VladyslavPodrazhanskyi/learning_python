from pprint import pprint
from sys import getsizeof, version_info, version

my_range = range(1_000_000_000_000)
print(range.__mro__)

# print(f"range: {getsizeof(range(1_000_000_000_000))}")
# print(f"iter_range: {getsizeof(iter(range(1_000_000_000_000)))}")
# print(f"gen_range: {getsizeof((i for i in range(1_000_000_000_000)))}")
# print(f"list_range: {getsizeof(list(range(1_000_000_00)))}")

print(version)