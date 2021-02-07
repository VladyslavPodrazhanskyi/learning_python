class Test:
    def __init__(self):
        pass

    def double(self, x):      # имеет только один неявный аргумент  - self - instance of the class
        print("Multiple 2")   # доступ только из инстанса, нет доступа из класса.
        return x*2

# Оба декоратора позволяют получить доступ к методу не создавая экземпляр класса.

    @classmethod              # возвращает метод класса вместо метода инстанса (доступ из класс и инстанса)
    def triple(cls, x):       # принимает 1 неявный аргумент -  cls - Class
        print("Multiple 3")
        return x*3

    @staticmethod            # возвращает функцию с доступом как из инстанса, так и из класса.
    def quad(x):             # не имеет неявных аргументов, но доступ только из инстанса или класса.
        print("Multiple 4")
        return x*4

my_test = Test()

print("USE instance method double()")
try:
    print(double(10))
except NameError:
    print("You have no access to the instance method without instance\n")

print(my_test.double(10))  # access from instance

try:
    print(Test.double(10))   # access from class
except TypeError:
    print("You have no access to instance method from Class\n")

print("Use class method triple()\n")

try:
    print(triple(10))
except NameError:
    print("You have no access to the class method without class\n")

try:
    print(my_test.triple(10))  # access from instance
    print("You have access to the class method from an instance\n")
except TypeError:
    print("You have no access to the class method from instance.\n")

print(Test.triple(10))
print("You have access to the class method from the class\n")


print("Use static method quad()\n")

try:
    print(quad(10))
except NameError:
    print("You have no access to the static method without class\n")

try:
    print(my_test.quad(10))  # access from instance
    print("You have access to the static method from an instance\n")
except TypeError:
    print("You have no access to the static method from instance.\n")

print(Test.quad(10))
print("You have access to the static method from the class\n")

print(my_test.double)   # <bound method Test.double of <__main__.Test object at 0x7f318f636748>>
print(my_test.triple)   # <bound method Test.triple of <class '__main__.Test'>>
print(my_test.quad)     # <function Test.quad at 0x7f318f632ea0>

print('########################################################################')



test1 = Test()
res = test1.quad(435)
print(res)


