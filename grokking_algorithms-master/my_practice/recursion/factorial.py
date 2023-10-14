def factorial(i: int) -> int:
    if i == 0:
        return 1
    return i * factorial(i - 1)


if __name__ == '__main__':
    print(factorial(20))
    # for i in range(11):
    #     print(factorial(i))
