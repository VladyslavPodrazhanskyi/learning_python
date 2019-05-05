# 1. Определеям внешнюю функцию.
def outer_func():
# 2. Внутри внешней определяем внутреннюю функцию.
    def inner_func():
        print("I'm an inner func!")
# 3. Внутри внешней вызываем внутреннюю функцию.
    inner_func()

# 4. Вызываем внешнюю функцию, внутри ее происходит вызов внутренней функции и результат выводится на экран.
# внутренняя функция не существует вне внешней и напрямую ее вызвать нельзя.
outer_func()
