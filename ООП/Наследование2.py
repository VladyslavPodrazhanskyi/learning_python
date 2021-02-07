# Родительский класс
class Shape:
# Атрибуты родительского класса
# они наследуются дочерним классом
    def __init__(self, w, l):
        self.width = w
        self.length = l
    def print_size(self):
        print(''' {} на {}
                 '''.format(self.width,
                            self.length))
my_shape = Shape(24, 23)
my_shape.print_size()

# Дочерний класс
class Rectangle(Shape):
# Переопределение контруктора __init__:
    def __init__(self, w, l, color):
        super().__init__(w, l)     # или  Shape.__init__(self, w, l)
        self.color = color

# метод дочернего класс, не затрагивающий
# родительский класс.
    def area(self):
        return self.width*self.length
# Переопределение родительского метода
    def print_size(self):
        print(''' Прямоугольник {} на {}, color {} 
                 '''.format(self.width,
                            self.length, self.color))
    


my_rec= Rectangle(20, 20, 'red')
my_rec.print_size()   # вызов переопределенного метода
print(my_rec.area()) # вызов и вывод на экран
# дочернего метода.

