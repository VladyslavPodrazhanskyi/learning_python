def is_pallindrome(num):
    if num // 10 == 0:
        return False
    cur = num
    rev = 0
    while cur != 0:
        rev = rev * 10 + cur % 10
        cur = cur // 10
    if num == rev:
        return True
    return False


# print(is_pallindrome(313))


def inf_polidromes():
    num = 0
    while True:
        if is_pallindrome(num):
            i = yield num
            if i is not None:
                num = i
        num += 1


pol_gen = inf_polidromes()

for item in pol_gen:
    print(item)
    digits = len(str(item))
    if digits >= 5:
        pol_gen.close()

