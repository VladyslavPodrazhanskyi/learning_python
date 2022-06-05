from typing import List


def binary(n: int) -> List[int]:
    bin_list = []

    def convert(n: int) -> List[int]:
        if n == 0:
            return bin_list
        bin_list.append(n % 2)
        return convert(n // 2)

    return convert(n)[::-1]


print(binary(23))


