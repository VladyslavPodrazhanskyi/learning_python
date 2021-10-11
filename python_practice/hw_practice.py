class C:
    def __init__(self):
        self.__x = 0

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, v):
        self.__x = v

    @x.deleter
    def x(self):
        del self.__x


