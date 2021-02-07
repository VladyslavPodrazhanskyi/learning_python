 # создание класса
class Orange:
 # создание полей
    def __init__ (self, w, c):    
        self.weight = w
        self.color = c
        self.mold = 0
# создание метода, кот меняет поле mold
    def rot(self, t, d):
        self.mold =  t*d
# контроль создания класса
        print('Создано!')
# создние объекта с зад. знач полей
or1 = Orange(100, 'dark')
# вывод на печать значений полей
print(or1.color)
print(or1.weight)
print(or1.mold)
# вывод на печать объекта
#<__main__.Orange object at 0x022F8950>
print(or1)
# замена значения поля
or1.color = 'light'
print(or1.color)
# применение метода к экз. класса.
or1.rot(20,20)
print(or1.mold)
