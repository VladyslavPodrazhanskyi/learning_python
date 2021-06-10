class FiboIter:
    def __init__(self, stop):
        self.prev, self.cur = 0, 1
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.cur < self.stop:
            self.prev, self.cur = self.cur, self.prev + self.cur
            return self.prev
        raise StopIteration


fibo_iter = FiboIter(24)

for el in fibo_iter:
    print(el)

# print(next(fibo_iter))