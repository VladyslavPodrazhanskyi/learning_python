"""
https://www.programiz.com/python-programming/user-defined-exception

When we are developing a large Python program,
it is a good practice to place all the user-defined exceptions
that our program raises in a separate file.
Many standard modules do this.
They define their exceptions separately as exceptions.py or errors.py
"""


class Error(Exception):
    """Base class for other exceptions"""
    pass


class ValueTooSmallError(Error):
    """Raise is the input value is too small"""
    pass


class ValueTooLargeError(Error):
    """Raise is the input value is too large"""
    pass


def input_int(message: str) -> int:
    while True:
        try:
            number = int(input(message))
            break
        except ValueError as ve:
            print(ve)
    return number


target_number = input_int('Enter int number to quess: ')

while True:
    try:
        guess = input_int('Guess target int number: ')
        if guess < target_number:
            raise ValueTooSmallError
        elif guess > target_number:
            raise ValueTooLargeError
        break
    except ValueTooSmallError:
        print('This value is too small')
        print()
    except ValueTooLargeError:
        print('This value is too large')
        print()

print(f'Congratulation, you guessed number {guess}')




