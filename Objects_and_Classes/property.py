class C:
    def __init__(self):
        self.__x = 22

    @property
    def x(self):
        print('Retrieve var __x')
        return self.__x

    @x.setter
    def x(self, value):
        print("Update var __x")
        self.__x = value

    @x.deleter
    def x(self):
        print("Deleting var __x")
        del self.__x

    



c = C()

print(c.x)
c.x = 25
print(c.x)