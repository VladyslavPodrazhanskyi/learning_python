class MySequence:
    def __init__(self, stop_iter):
        self.stop = stop_iter

    def __getitem__(self, key):
        if key > self.stop:
            raise KeyError
        return key * 10


my_seq = MySequence(10)
print(dir(my_seq))

my_list = [10*x for x in range(11)]


my_iter = iter(my_seq)

print(dir(my_iter))
print(dir(my_list))


#
# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))
