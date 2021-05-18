""""os.path
Подмодуль os.path модуля os имеет широкий ряд встроенных преимуществ. Ознакомимся со следующими функциями:

basename
dirname
exists
isdir and isfile
join
split
"""

import os

# name

print(os.name)

# environ

for k in os.environ:
    print(k, os.environ[k])
print(type(os.environ))

print(os.getcwd())
