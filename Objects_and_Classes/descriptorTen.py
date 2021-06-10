class Ten:
    def __get__(self, obj, type=None):
        return 10

    def __set__(self, obj, value):
        raise AttributeError("Cannot change the Value!")


class A:
    x = 10
    y = Ten()


a = A()


print(a.x)
print(a.y)
a.x = 20
print(a.x)
# a.y = 20

setattr(a, "y", 50)
print(a.y)


