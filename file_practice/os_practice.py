import os

print(os.name) # posix
print(os.getcwd())

file = os.popen(
    '/home/vladyslav_podrazhanskyi/projects/python/learning_python/file_practice/file4.txt', 'w'
)  # Permission denied
file.write('Hello')
