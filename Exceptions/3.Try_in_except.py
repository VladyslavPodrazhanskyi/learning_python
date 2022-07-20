"""
try:
    code with possible exception
    stop running at the line
    with the first exception
except exception1 as e1:
    code if exception1 is raised
except exception2 as e2:
    code if exception2 is raised
else:
    if there are no any exception
finally:
    this code is running at any case
    ( even if some exception was not caught)

code -
continue program:
 if there are no exception  ( as else)
 if exception was caught by except
===================================
work with files ( with -  context manager is better option):

try:

finally:

"""



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