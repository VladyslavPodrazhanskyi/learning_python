"""
https://pythonist.ru/sobiraem-i-razbiraem-stroku/
"""

from typing import List


def construct_deconstruct(string_data: str) -> List[str]:
    first = [string_data[:i] for i in range(1, len(string_data) - 1)]
    return first + [string_data] + first[::-1]

    # res_list = []
    # for i in range(len(string_data)):
    #     res_list.append(string_data[:i+1])
    # for j in range(len(string_data) - 1):
    #     res_list.append(string_data[:-1-j])
    # return res_list





print(construct_deconstruct('the sun'))