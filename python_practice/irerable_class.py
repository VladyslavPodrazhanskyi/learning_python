class MySequence:
    def __init__(self, stop):
        self.stop = stop

    def __getitem__(self, key):
        if key > self.stop:
            raise IndexError("That's enough!")
        return key * 10

my_seq = MySequence(5)

my_iter = iter(my_seq)


print(my_seq, type(my_seq))
print(my_iter, type(my_iter))


print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))