# Итераторы -  объект в котором прописоно метод __next__
# итерируемый (iterable) - объект по которому можно итерироваться
# итерация  -  каждое действие по циклу.




# большой объект занимает много памяти, работа с ним сильно
# тормозит код
# generators - объект, при обращении к нему методом next возвращает
# след значение и не хранит весь объем данных.
# ключевое слово - yield
# генератором может быть любая функция в которой прописан yield c циклом.

def gen():
    x = 1
    while True:
        yield x**2
        x += 2

our_gen = gen()

# for i in range(100):
#     step_value = next(our_gen)
#     print(step_value)


import sys

def gen_100000():
    x = 0
    while x < 100000:
        yield x
        x += 1

gen_test_size = gen_100000()
gen_expres_test_size = (x for x in range(100000))
list_test_size = list(range(100000))


print(type(gen_test_size))
print(type(gen_expres_test_size))
print(type(list_test_size))

print(sys.getsizeof(gen_test_size))
print(sys.getsizeof(gen_expres_test_size))
print(sys.getsizeof(list_test_size))