from time import time
from random import randint

def benchmark(function):
    def wrapper(data):
        start = time()
        value = function(data)
        end = time()
        print(f'Execution time:{end - start}')
        return value
    return wrapper


@benchmark
def sorting(data):
    for i in range(len(data) - 1):
        for j in range(len(data) - 1 - i):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
    return data


# sorting = benchmark(sorting)


d = [randint(-25, 25) for _ in range(1000)]

sorting(d)