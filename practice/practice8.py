from typing import List


def filter_data(data: List[int], filter_key: int):
    if filter_key and isinstance(filter_key, int):
        data = [num for num in data if num % filter_key == 0]
    return data


my_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(filter_data(my_data, 6))
