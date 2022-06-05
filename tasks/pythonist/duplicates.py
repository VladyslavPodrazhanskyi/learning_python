"""
https://pythonist.ru/schitaem-povtory/
"""


def duplicates(txt: str) -> int:
    # return sum([
    #     txt.count(txt[i]) - 1
    #     for i in range(len(txt))
    #     if txt[i] not in txt[:i]
    # ])
    return len(txt) - len(set(txt))


assert duplicates('Hello World!') == 3
assert duplicates('foobar') == 1
assert duplicates('helicopter') == 1
assert duplicates('birthday') == 0
