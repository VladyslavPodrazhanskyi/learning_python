"""
В функции fun1() объявлена локальная переменная x,
значение которой определяется аргументом a.
В функции fun2() используются эта же переменная x, nonlocal указывает на то,
что эта переменная не является локальной, следовательно, ее значение будет взято
из ближайшей области видимости, в которой существует переменная с таким же именем.
В нашем случае – это область enclosing, в которой этой переменной x присваивается значение a * 3.
Также как и в предыдущем случае, на переменную x после вызова fun1(4), сохраняется ссылка,
поэтому она не уничтожается.

"""


def fun1(a):
    x = a * 3

    def fun2(b):
        nonlocal x
        return b + x

    return fun2
