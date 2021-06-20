from typing import List, Dict, Union, Generator
from random import randint

# We will work with such dicts
ST = Dict[str, Union[str, int]]
# And we will put this dicts in list
DT = List[ST]

dt = [{'name': 'alex', 'age': 26}, {'name': 'denys', 'age': 89}]
print(f'dt: {dt}')
def task_1_fix_names_start_letter(data):
    """
    Make all `names` field in list of students to start from upper letter

    Examples:
        fix_names_start_letters([{'name': 'Alex', 'age': 26}, {'name': 'denys', 'age': 89}])

    """
    def cap_func(x):
        y = x.copy()
        y['name'] = y['name'].capitalize()
        return y

    cap_data = list(map(cap_func, data))
    return cap_data


print(task_1_fix_names_start_letter(dt))

def task_2_remove_dict_fields(data, k):
    """given_data
    Remove from dictionaries given key value

    """
    def del_el(d):
        if k in d:
            del d[k]
        return d

    updated_data = list(map(del_el, data))
    return updated_data


# print(task_2_remove_dict_fields(dt, 'age'))
print(dt)

def task_3_find_item_via_value(data, value):
    """
    Find and return all items that has @searching value in any key
    Examples:
        find_item_via_value([{'name': 'Alex', 'age': 26}, {'name': 'denys', 'age': 89}], 26)

    """

    return list(filter(lambda x: value in x.values(), data))

print(task_3_find_item_via_value(dt, 26))





def task_4_min_value_integers(data: List[int]) -> int:
    """
    Find and return minimum value from list
    """
    return min(data)

test_list = [randint(-25, 45) for _ in range(25)]
print(test_list)
print(task_4_min_value_integers(test_list))


def task_5_max_value_strings(data: List[Union[str, int]]) -> str:
    """
    Find the longest string
    """
    el_max = data[0]
    for i in range(1, len(data)):
        if len(data[i]) > len(el_max):
            el_max = data[i]
    return el_max


data_list = ['fsjfo', 'k', 'skjfsdfj', 'fsjfo', 'kfdssdgfsdgsgsdgggghdh', 'skjfsdfj']
print(task_5_max_value_strings(data_list))

def task_6_min_value_list_of_dicts(data: DT, key: str) -> ST:
    """
    Find minimum value by given key
    Returns:

    """
    pass


def task_7_max_value_list_of_lists(data: List[List[int]]) -> int:
    """
    Find max value from list of lists
    """
    pass


def task_8_sum_of_ints(data: List[int]) -> int:
    """
    Find sum of all items in given list
    """
    pass


def task_9_sum_characters_positions(text: str) -> int:
    """
    Please read first about ascii table.
    https://python-reference.readthedocs.io/en/latest/docs/str/ASCII.html
    You need to calculate sum of decimal value of each symbol in text

    Examples:
        task_9_sum_characters_positions("A")
        >>> 65
        task_9_sum_characters_positions("hello")
        >>> 532

    """
    pass


def task_10_generator_of_simple_numbers() -> Generator[int, None, None]:
    """
    Return generator of simple numbers
    Stop then iteration if returned value is more than 200
    Examples:
        a = task_10_generator_of_simple_numbers()
        next(a)
        >>> 2
        next(a)
        >>> 3
    """
    return (range)


def task_11_create_list_of_random_characters() -> List[str]:
    """
    Create list of 20 elements where each element is random letter from latin alphabet

    """
    pass
