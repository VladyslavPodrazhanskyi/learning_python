"""
Python automatically closes a file
when the reference object of a file is reassigned to another file.
It is a good practice
to use the close() method to close a file

r -  read
write -  w
append - a
exclusive creation - x

"""

with open('file4.txt', 'w', encoding='utf-8') as f:
    f.write('new content1')
    f.write('\n')
    f.write('new content3')
    print("Name of the file: ", f.name)
    print("Closed or not : ", f.closed)
    print("Opening mode : ", f.mode)
print(f.closed)

with open('file1.txt') as f:
    content_ten = f.read(10)
    print(content_ten)
    print(f.tell())
    print(f.seek(15))
    print(f.tell())


try:
    f = open('file1.txt')
    print('content string')
    print(f.read())
    print(5 / 0)
except ZeroDivisionError as ze:
    print(ze)
finally:
    f.close()
