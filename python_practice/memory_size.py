import sys


big_list = [x for x in range(100000)]
big_gen = (x for x in range(100000))

class SomeSeq:
    def __init__(self, stop):
        self.stop = stop

    def __getitem__(self, k):
        if k > self.stop:
            raise IndexError
        return k * 10

seq = SomeSeq(100000)

print(seq[99999])

print(sys.getsizeof(seq))
print(sys.getsizeof(big_list))
print(sys.getsizeof(big_gen))