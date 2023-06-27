"""
Typеcоdе Vаluе
b Rеprеsеnts signеd intеgеr оf sizе 1 bytе
B Rеprеsеnts unsignеd intеgеr оf sizе 1 bytе
c Rеprеsеnts chаrаctеr оf sizе 1 bytе
i Rеprеsеnts signеd intеgеr оf sizе 2 bytеs
I Rеprеsеnts unsignеd intеgеr оf sizе 2 bytеs
f Rеprеsеnts flоаting pоint оf sizе 4 bytеs
d Rеprеsеnts flоаting pоint оf sizе 8 bytеs
"""

import array

array1 = array.array('i', [10, 20, 30, 40, 50])

for el in dir(array):
    print(el)

print(type(array1))
print(array1)

array1.insert(1, 60)

remove_from_array = [55, 40]

for rel in remove_from_array:
    try:
        array1.remove(rel)
    except ValueError as er:
        print(rel, er)


for x in array1:
    print(x)


# search operation
print(array1.index(30))

# update (reassign element)
array1[4] = 11

print(array1)
