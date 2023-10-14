import random
from typing import List

random.seed(2)


def generate_test_data(len: int) -> List[int]:
    return [
        random.randint(0, 1000)
        for _ in range(len)
    ]


def generate_batches(data: List[int], max_len: int = 100) -> List[List[int]]:
    batches = []
    while len(data) > max_len:
        batches.append(data[:max_len])
        data = data[max_len:]
    batches.append(data)
    return batches


def generate_batches_recur(data: List[int], max_len: int = 100) -> List[List[int]]:
    if len(data) <= max_len:
        return [data]
    else:
        first_part = data[:max_len]
        remain_part = data[max_len:]
        batches = generate_batches_recur(remain_part, max_len)
        return [first_part] + batches


if __name__ == '__main__':

    test_list = generate_test_data(201)

    batches = generate_batches(test_list)
    batches_recur = generate_batches_recur(test_list)

    print("batches")
    for batch in batches:
        print(batch)

    print("batches_recur")
    for batch in batches_recur:
        print(batch)

    print(batches == batches_recur)
