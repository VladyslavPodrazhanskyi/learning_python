class FiboIterator:
    def __init__(self, stop):
        self.prev, self.cur = 0, 1
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.cur < self.stop:
            self.prev, self.cur = self.cur, self.cur + self.prev
            return self.prev

        else:
            raise StopIteration


fibo_iter = FiboIterator(23)

print(next(fibo_iter))
print(next(fibo_iter))
print(next(fibo_iter))
print(next(fibo_iter))
print(next(fibo_iter))
print(next(fibo_iter))