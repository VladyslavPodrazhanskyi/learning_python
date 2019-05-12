# Запись в пустой файл
# Режимы открытия файла  -  "r" - default, "w", "a" - присоединение, "r+" - чтение и запись.
# "w" -  создает файл, если он не существует, записывает новую информацию стирая старую,
# если такой файл существует

file_path  = "programming.txt"

with open(file_path, "w") as file_object:
    file_object.write("I love programming!")  # информация для записи в файл должна быть string.
    file_object.write("\nPython is my favorite programming language!") # 2 строки склеились друг с другом.
# for separation lines add \n in string of second line.


# Присоединение данных к файлу:
with open(file_path, "a") as file_object:
    file_object.write("\nI want to be the best python programmer in the Wordl!")