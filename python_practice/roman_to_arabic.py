"""
Write a function converting a Roman numeral from a given string N into an Arabic numeral.
Values may range from 1 to 100 and may contain invalid symbols.
Invalid symbols and numerals out of range should raise ValueError.

Numeral / Value:
I: 1
V: 5
X: 10
L: 50
C: 100

Example:
N = 'I'; result = 1
N = 'XIV'; result = 14
N = 'LXIV'; result = 64

Example of how the task should be called:
python3 task_3_ex_2.py LXIV

Note: use `argparse` module to parse passed CLI arguments
"""

import argparse

parser = argparse.ArgumentParser()

parser.add_argument('roman', type=str, help='input roman number to translate in arabic')


def from_roman_numerals(roman):
    roman_dict = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100
    }
    for el in roman:
        if el not in roman_dict:
            raise ValueError
    res = roman_dict[roman[-1]]
    for i, cur in enumerate(roman[:-1]):
        # check that there are not more than 1 of roman symbols of less value before the symbol in roman number
        if i < len(roman) - 2 and roman_dict[cur] < roman_dict[roman[i + 2]]:
            raise ValueError

        if roman_dict[cur] < roman_dict[roman[i + 1]]:
            res -= roman_dict[cur]
        else:
            res += roman_dict[cur]

    if res > 100:
        raise ValueError
    return res


    # for i, cur in enumerate(roman):
    #     for forward in roman[i + 1:]:
    #         if roman_dict[forward] > roman_dict[cur]:
    #             res -= roman_dict[cur]
    #             break
    #     else:
    #         res += roman_dict[cur]
    # if res > 100 or res < 0:
    #     raise ValueError
    # return res


def main():
    args = parser.parse_args()
    roman = args.roman
    print(from_roman_numerals(roman))


if __name__ == '__main__':
    main()


# def from_roman_numerals(roman):
#     roman_dict = {
#         "I": 1,
#         "V": 5,
#         "X": 10,
#         "L": 50,
#         "C": 100
#     }
#     # check that all chars in input string contain only roman digits
#     for char in roman:
#         if char not in roman_dict:
#             raise ValueError
#     # calculate arabic from roman:
#     arabic = 0
#     for i in range(len(roman)):
#         if i > 0 and roman_dict[roman[i]] > roman_dict[roman[i - 1]]:
#             arabic += roman_dict[roman[i]] - 2 * roman_dict[roman[i - 1]]
#         else:
#             arabic += roman_dict[roman[i]]
#     # check if arabic number not more than 100.
#     if arabic <= 100:
#         return arabic
#     else:
#         raise ValueError