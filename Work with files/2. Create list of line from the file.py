# Read of whole file

file_name = "test_file.txt"   # file_path should be used in general

# with - context manager ( as file_objecr- allias for open(file_name).
# open(file_path, "r") - returns object(file) with rights read, write...
with open(file_name) as file_object:
    contents = file_object.read()           # method read() -  returns content of whole file
    print(contents)
print("\n")

# Read separate lines of the file.
with open(file_name) as file_object:
    for line in file_object:   # in - запускает __contains__
        print(line, end="")                       # который считывает построчно содержимое файла без метода read

# we have empty line after every line of the text.
# так каждая строка файла заканчивается невидимым символом перехода на новую строку
# функция print -  добавляет еще свой символ новой строки после вывода строки на экран.
# настроив print - устраняем пустые лишние строки.

