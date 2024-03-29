"""
Вызывая nmul5(2), мы фактически обращаемся к функции helper(),
которая находится внутри mul(). Переменная a, является локальной для mul(),
и имеет область enclosing в helper(). Несмотря на то, что mul() завершила свою работу,
переменная a не уничтожается, т.к. на нее сохраняется ссылка во внутренней функции,
которая была возвращена в качестве результата.
"""


def mul(a):
    def helper(b):
        return a * b

    return helper


print(mul(5)(2))

mul5 = mul(5)

print(mul5.__closure__)

print(mul5(7))


def some_func(arg):
    return arg * 3


