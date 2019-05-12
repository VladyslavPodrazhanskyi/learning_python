# Вывести на экран содержимое файла одной строкой.

file_path = "test_file.txt"

with open(file_path) as file_object:
    lines = file_object.readlines()    # список строк, в каждой строке есть \n

lines = [line.rstrip() for line in lines]  # создаем список строк без \n
one_string = " ".join(lines)
print(one_string)             # из списка строко создаем строку, слова разделяем пробелами


# Альтернативное решение:

# one_string = ""
# for line in lines:
#     one_string += line.rstrip() + " "
#
# print(one_string)