# file = open('test.txt')
# print(file.read())
# file.close()
import os
#
# file = open('test.txt', 'x')
# file.write('oio')
# file.close()
if os.path.exists('test.txt'):
    file = open('test.txt')
    print(file.read())
    file.close()
    os.remove('test.txt')
else:
    file = open('test.txt', 'w')
    file.write('''
    sfjksdfjk
    sfkjjfksjfjks
    ksjfkfjffskfksjf
    ''')
    file.close()


