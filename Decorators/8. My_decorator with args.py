def new_decorator(func):
    def wrapper(*args):
        print("Принимаю от функции аргументы и делю их на 2")
        return [x/2 for x in func(*args)]

    return wrapper

@new_decorator
def square(*args):
    return [x**2 for x in args]

print(square(*list(range(25))))