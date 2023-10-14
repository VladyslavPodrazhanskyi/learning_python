from typing import List


def define_min_ind(data: List[int]) -> int:
    min_ind = 0
    for i in range(len(data)):
        if data[i] < data[min_ind]:
            min_ind = i
    return min_ind


def selection_sort(data: List[int]) -> List[int]:
    sorted = []
    while data:
        sorted.append(data.pop(define_min_ind(data)))
    return sorted


if __name__ == '__main__':
    print(selection_sort([45, 11, 3, 7, 34, 67, -1]))
