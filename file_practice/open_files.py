with open('file1.txt', 'w') as f:
    f.write('new content')

with open('file1.txt') as f:
    content = f.read()

print(content)