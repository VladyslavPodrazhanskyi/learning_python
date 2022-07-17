import sys


def linux_function():
    assert 'linux' in sys.platform, 'This functions runs only in Linux OS'
    print('linux_function is running')


try:
    linux_function()
except AssertionError as as_er:
    print(as_er)
else:
    try:
        with open('some_file') as file_object:
            contents = file_object.read()
            print(contents)
    except FileNotFoundError as fnf_error:
        print(fnf_error)
finally:
    print('Cleaning up, irrespective of any exceptions.')