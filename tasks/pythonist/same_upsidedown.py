"""
https://pythonist.ru/perevorot/
"""


def same_upsidedown(str_number: str) -> bool:
    pairs = ['00', '69', '96']
    return all([(str_number[i] + str_number[-i-1]) in pairs for i in range(len(str_number))])


assert same_upsidedown("6090609")
assert not same_upsidedown("9669")
assert same_upsidedown("69069069")
