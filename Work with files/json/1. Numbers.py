import json
#
# numbers_list = [2, 3, 4, 242, 1, 6, 353, 54]
# numbers_tuple = (12, 43, 24, 521, 5211)
#
# # Сохранение списка чисел в json файле.
#
file_path1 = "numbers_list.json"
# with open(file_path1, "w") as file_object:
#     json.dump(numbers_list, file_object)
#
# # Сохранение кортежа чисел в json файле.
#
file_path2 = "numbers_tuple.json"
# with open(file_path2, "w") as file_object:
#     json.dump(numbers_tuple, file_object)

# Загрузка списка чисел из json файла.

with open(file_path1) as file_object:
    loaded_list = json.load(file_object)

print(loaded_list)

with open(file_path2) as file_object:
    loaded_tuple = json.load(file_object)

print(loaded_tuple)                           # json преобразовал кортеж в список.