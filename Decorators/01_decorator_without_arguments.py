def decor(f):
    def wrapper():
        print('code before')
        f()
        print('code after')

    return wrapper


@decor               # square = decor(square)
def square():
    print ('hello')


square()


