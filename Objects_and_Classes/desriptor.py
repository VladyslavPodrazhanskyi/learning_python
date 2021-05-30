class RevealAccess():
    def __init__(self, initval=None, name='var'):
        self.val = initval
        self.name = name

    def __get__(self, obj, objtype):
        print('Retrieving', self.name)
        return self.val

    def __set__(self, obj, value):
        print('Updating', self.name)
        self.val = value


class MyClass:
    x = RevealAccess(10, 'var x')
    y = 5

class Def:
    pass



print('def:', dir(Def))
print('myclass', dir(MyClass))
print('reveal', dir(RevealAccess))


m = MyClass()

print(m.x)
m.x = 20

print(m.x)
print(m.y)