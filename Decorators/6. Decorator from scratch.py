separator = "\n" + "+"*20 + "\n"

# Block 1 is equal to:

def decorator(decorated_func):
    def wrapper():
        return decorated_func() + "=" + str(eval(decorated_func()))

    return wrapper


def decorated_func():
    return str(1) + "+" + str(1)

print(decorator(decorated_func)())


print(separator)

# Block 2

@decorator
def decorated_func():
    return str(1) + "+" + str(1)

print(decorated_func())

