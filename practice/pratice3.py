# decorator
def tagh1(func):
    def wrapper(*args):
        return f'<h1>{func(*args)}</h1>'

    return wrapper


@tagh1  # use decorator to decorate function greeting
def greeting(name):
    return f'Hello, {name}!'


# function greeting2 is not decorated
def greeting2(name):
    return f'Hello, {name}!'


print(greeting('Igor'))
print(greeting2('Igor'))
