import sys

try:
    assert 5 == 2, '5 != 2'
except AssertionError as error:
    print(error)

try:
    print(5 / 0)
except ZeroDivisionError as e:
    print(e)
else:
    print('There are no exception')
finally:
    print('finally')

print('After else')


try:
    with open('file_log') as f:
        read_data = f.read()
except FileNotFoundError as fnf_er:
    print(fnf_er)