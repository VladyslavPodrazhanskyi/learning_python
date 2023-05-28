from multiprocessing import Process, cpu_count


def print_square(num):
    print(f"square of {num} is equal {num ** 2}")


num = 5

proc = Process(target=print_square, args=(num, ))

proc.start()
