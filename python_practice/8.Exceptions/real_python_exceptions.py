'''customs exception:'''
# x = 10
# if x > 5:
#     raise Exception('x should not exceed 5. The value of x: {}'.format(x))


'''assert for debagging'''
# x = 10
# assert x < 5, 'x should not exceed 5. The value of x: {}'.format(x)


'''handling AssertionError'''
# try:
#     x = 10
#     assert x < 5
# except AssertionError:
#     print('x should not exceed 5. The value of x: {}'.format(x))

'''assert sample'''
# import sys
#
# print(sys.platform) # win32
# assert ('linux' in sys.platform), 'This code runs on Linux only.'

'''The try and except Block: Handling Exceptions
The try and except block in Python is used to catch and handle exceptions. 
Python executes code following the try statement as a “normal” part of the program. 
The code that follows the except statement is the program’s response to any exceptions 
in the preceding try clause.'''

import sys

def linux_interaction():
    assert('linux' in sys.platform), "Function can only run on Linux systems."
    print('Doing something')

def windows_interaction():
    assert('win' in sys.platform), "Function can only run on Windows systems."
    print('Doing something')

# windows_interaction()
# linux_interaction()
#
# try:
#     linux_interaction()
# except AssertionError as error:
#     print(error)
#     print("Linux function was not executed")
#
# try:
#     windows_interaction()
# except AssertionError:
#     print("windows function was not executed")

'''try-except-else-finally'''

try:
    windows_interaction()    #  linux_interaction()
except AssertionError as error:
    print(error)
    print("Linux function was not executed")
else:
    try:
        with open('file.log') as file:
            file.read()
    except FileNotFoundError as fnf_error:
        print(fnf_error)
finally:
    print('Cleaning up, irrespective of any exceptions')

