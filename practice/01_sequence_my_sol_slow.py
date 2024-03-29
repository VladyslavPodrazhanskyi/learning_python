# Lessons from https://stepik.org/
# 2. Циклы. Строки. Списки.
# Задача 2.6.3
# Date 24.10.2022

# Напишите программу, которая выводит часть последовательности 1 2 2 3 3 3 4 4 4 4 5 5 5 5 5 ...
# (число повторяется столько раз, чему равно). На вход программе передаётся неотрицательное целое
# число n - столько элементов последовательности должна отобразить программа. На выходе ожидается
# последовательность чисел, записанных через пробел в одну строку.
#
# Например, если n = 7, то программа должна вывести 1 2 2 3 3 3 4.

def sequence(number: int):
    res_list = []
    for i in range(int(number * (number + 1) / 2)):
        res_list += [i] * i
    return ' '.join([str(el) for el in res_list])


if __name__ == '__main__':
    print(sequence(1))

#
#
#
# n, string = int(input()), ""
# for i in range(1, n + 1):
#     string += (str(i) + " ") * i
# print(string[:n * 2].strip())