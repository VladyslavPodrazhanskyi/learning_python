from functools import wraps


def h1_decor(func):
    @wraps(func)
    def wrapper(*args):
        return f'<h1>{func(*args)}</h1>'
    return wrapper


def tag_decor(tag):   # prefix
    def decorator(func):   # decorator
        @wraps(func)
        def wrapper(*args):   # wrapper
            return f'<{tag}>{func(*args)}</{tag}>'
        return wrapper
    return decorator


# @h1_decor
@tag_decor('h2')
def greeting(name):
    return f'Hello, {name.title()}!'






print(greeting.__name__)
print(greeting('mila'))
