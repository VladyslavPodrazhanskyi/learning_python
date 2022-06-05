"""
https://pythonist.ru/pary-bukv/
"""


def str_match_by2char(first: str, second: str) -> int:
    res = 0
    for i in range(min(len(first), len(second)) - 1):
        if first[i] == second[i] and first[i + 1] == second[i + 1]:  # if first[i:i+2] == second[i:i+2]
            res += 1
    return res


assert str_match_by2char("yytaazz", "yyjaaz") == 3
assert str_match_by2char("edabit", "ed") == 1
assert str_match_by2char("", "") == 0
