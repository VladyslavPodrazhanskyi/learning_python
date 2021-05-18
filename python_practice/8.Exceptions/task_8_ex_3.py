def baz():
    try:
        return 1
        with open("/tmp/logs.txt") as file:
            print(file.read())
            return
    finally:
        return 2


result = baz()
print(result)
