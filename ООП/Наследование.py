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
class Square(Shape):
# метод дочернего класс, не затрагивающий
# родительский класс.
    def area(self):
        return self.width*self.length
# Переопределение родительского метода
    def print_size(self):
        print(''' Квадрат {} на {}
                 '''.format(self.width,
                            self.length))
    


my_square= Square(20,20)
my_square.print_size()   # вызов переопределенного метода
print(my_square.area()) # вызов и вывод на экран
# дочернего метода.
