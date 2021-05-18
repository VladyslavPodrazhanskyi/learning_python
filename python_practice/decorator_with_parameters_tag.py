from functools import wraps


def tag(type_tag):
    def decorator(func):
        @wraps(func)
        def wrapper(*args):
            return f'<{type_tag}>{func(*args)}</{type_tag}>'
        return wrapper
    return decorator

# @tag('p')
def full_name(first, second):
    return f'full name: {first} {second}'

print(full_name.__name__)

print(full_name('Bruce', 'Lee'))