"""
https://www.programiz.com/python-programming/user-defined-exception

When we are developing a large Python program,
it is a good practice to place all the user-defined exceptions
that our program raises in a separate file.
Many standard modules do this.
They define their exceptions separately as exceptions.py or errors.py
"""


class CustomsError(Exception):
    pass


def using_custom_error(x):
    if x > 100:
        return x * 3
    else:
        raise CustomsError


if __name__ == '__main__':
    using_custom_error(120)
