import functools

user = {"username": "Jose", "access_level": "guest"}


def secure_get_admin(level_access):
    def decorator(fn):
        @functools.wraps(fn)
        def wrapper(*args, **kwargs):
            if user['access_level'] == level_access:
                return fn(*args, **kwargs)
            else:
                return f'No permissions for {user["username"]}'
        return wrapper
    return decorator


@secure_get_admin('admin')
def get_admin_password():
    return "admin: 1234"


@secure_get_admin('user')
def get_dashboard_password():
    return "user: user_password"



print(get_admin_password())
print(get_dashboard_password)


