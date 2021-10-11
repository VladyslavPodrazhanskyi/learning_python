import functools

user = {"username": "Jose", "access_level": "admin"}


def secure_get_admin(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        if user['access_level'] == 'admin':
            return fn(*args, **kwargs)
        else:
            return f'No permissions for {user["username"]}'
    return wrapper


@secure_get_admin
def get_admin_password(panel):
    if panel == "admin":
        return '1234'
    elif panel == "billing":
        return 'super_secure_password'


# get_admin_password = secure_get_admin(get_admin_password)

print(get_admin_password('billing'))
print(get_admin_password.__name__)   # wrapper without @functools.wraps(fn)
# get_admin_password with @functools.wraps(fn)