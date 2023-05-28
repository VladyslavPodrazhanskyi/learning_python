"""
https://realpython.com/python-scope-legb-rule/

You use ex as an auxiliary variable to hold a reference
to the exception raised by the try clause.
This can be useful when you need to do something
with the exception object once the code block has finished.
Note that if no exception is raised, then ex remains None.


"""

er = None
try:
    print(4 / 0)
except ZeroDivisionError as error:
    er = error

print(er)
