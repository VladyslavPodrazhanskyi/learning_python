from random import randrange


def random_list():
    return [randrange(0, 100) for _ in range(20)]
