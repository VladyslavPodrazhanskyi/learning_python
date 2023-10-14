from typing import Union, Optional, List


def binary_search(
    sort_data: List[Union[int, str]],
    value: Union[str, int]
) -> Optional[int]:
    low_lim = 0
    top_lim = len(sort_data) - 1
    while low_lim <= top_lim:
        cur_middle = (low_lim + top_lim) // 2
        if sort_data[cur_middle] == value:
            return cur_middle
        if sort_data[cur_middle] > value:
            top_lim = cur_middle - 1
        else:
            low_lim = cur_middle + 1
    return


if __name__ == '__main__':
    print(binary_search([1, 3, 5, 7], 5))
    print(binary_search([1, 3, 5, 7], 11))
    print(binary_search(["a", "b", "ftor", "zoo"], "b"))
    print(binary_search(["a", "b", "ftor", "zoo"], "zoo"))
    print(binary_search(["a", "b", "ftor", "zoo"], "ftor"))
    print(binary_search(["a", "b", "ftor", "zoo"], "ft"))


