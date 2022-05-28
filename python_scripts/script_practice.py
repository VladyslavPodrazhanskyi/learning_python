#! /usr/bin/python

import sys
import os

"""
Running this code, you’ll get the list of directories
and .zip files where Python searches the modules 
you import.
"""
print("sys:")
for path in sys.path:
    print(path)



print("os:")
print(os.path)



from random import randint


data = [randint(0, 10) for _ in range(10)]
print(data)
print(list(set(data)))