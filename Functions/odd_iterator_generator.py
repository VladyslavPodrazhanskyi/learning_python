import sys

class OddIterator:
    def __init__(self):
        self.x = 1

    def __iter__(self):
        return self

    def __next__(self):
        cur, self.x = self.x, self.x + 2
        return cur


odd_iter = OddIterator()

# for i in range(50):
#     print(i, next(odd_iter))


def odd_gen():
    x = 1
    while True:
        yield x
        x += 2


odd_gen = odd_gen()

# for i in range(40):
#     print(i, next(odd_gen))

print(sys.getsizeof(odd_iter))
print(sys.getsizeof(odd_gen))
