"""
https://realpython.com/python-walrus-operator/
https://peps.python.org/pep-0572/

"""

inputs = []
while (current := input('Print something: ')) != 'quit':
    inputs.append(current)


