def fact(n: int) -> int:
    if n == 1:
        return 1
    return n * fact(n - 1)


if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        print(fact(int(sys.argv[1])))
