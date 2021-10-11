class OddNum:
    def __init__(self):
        self.next = 1

    def __iter__(self):
        return self

    def __next__(self):
        cur, self.next = self.next, self.next + 2
        return cur


infinite_iter = OddNum()

print(next(infinite_iter))
print(next(infinite_iter))
print(next(infinite_iter))
print(next(infinite_iter))
print(next(infinite_iter))
print(next(infinite_iter))
print(next(infinite_iter))
print(next(infinite_iter))
print(next(infinite_iter))