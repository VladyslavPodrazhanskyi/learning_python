# 1. Определеям внешнюю функцию.
def outer_func(outer_par="inner_func_1"):

# 1.1. Внутри внешней определяем 2 внутренних функции.
    def inner_func_1(inner_par = "word"):    # inner_func_1 возвращает аргумент + 1
        return inner_par + "1"
    def inner_func_2(inner_par = "word"):
        return inner_par + "2"                # inner_func_1 возвращает аргумент + 2

# 1.2. Если аргумент внешей функции совпадает с именем inner_func_1,
# то внешняя функция возвращает ИМЯ inner_func_1,
# иначе оно возвращает ИМЯ второй внутренней функции inner_func_2

    if outer_par == "inner_func_1":
        return inner_func_1         # name of inner_func_1
    else:
        return inner_func_2          # name of inner_func_2


# 2. Работа внешней функции:

# 2.1.Вызов внешней функци - возвращает имя функции inner_func_1,
# на экране ничего не происходит. Process finished with exit code 0
outer_func()
# тоже самое с использование дополнительного имени var = outer_func()
var = outer_func()

# 2.2. При выводе на экран внешней функции  -
# получаем объект функцию <function outer_func.<locals>.inner_func_1 at 0x7fb60b1dc048>
print(outer_func())
# тоже самое с использование дополнительного имени var
print(var)
# 2.3.  Вызов внутренней функции через внешнюю: outer() вызывает имя inner_func_1
# вторые скобки () вызывают функцию inner_func_1(),
# кот возвращает inner_par ( по умолчанию word) + 1
# 2.3.1. при этом на экран ничего не выводится.
outer_func()()
# тоже самое с использование дополнительного имени var
var()
# 2.3.2. На экран выводится значение возвращаемое внутренней функцией inner_func_1.
print(outer_func()())   # word1
# тоже самое с использование дополнительного имени var
print(var())
# 2.3.3. На экран выводится значение возвращаемое внутренней функцией inner_func_2.
print(outer_func("anything except - inner_func_1")())   # word2
# тоже самое с использование дополнительного имени var2
var2 = outer_func("anything except - inner_func_1")
print(var2())


