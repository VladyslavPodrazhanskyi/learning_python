union_dict = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine"
}

ten_twenty = {
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen"
}

ten_verbose = {
    2: "twenty",
    3: "thirty",
    4: "forty",
    5: "fifty",
    6: "sixty",
    7: "seventy",
    8: "eighty",
    9: "ninty"
}


def verbose_three(three_num):
    hundred = three_num // 100
    tens = three_num // 10 % 10
    units = three_num % 10
    if tens == 1:
        last_two = three_num % 100
        return f"{union_dict[hundred]} hundred {ten_twenty[last_two]}"
    return f"{union_dict[hundred]} hundred {ten_verbose[tens]} {union_dict[units]}"


def verbose_number(number):
    first_three = number // 1000
    second_three = number % 1000
    return f"{verbose_three(first_three)} thousand {verbose_three(second_three)}"


if __name__ == '__main__':
    print(verbose_number(765432))