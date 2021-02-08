a = True
b = True
c = False

print('True and False', '\n')

print(a or c)  # True
print(a and c)  # False

print('#####################################')

print('True, True and False', '\n')
print(a or b or c)    # True
print(a and b and c)  # False
print(a and b or c)    # True
print(a or b and c)    # True:  a or (b and c) - and first, or -  second
print((a or b) and c)  # False нарушил приоритет and