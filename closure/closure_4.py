def pow(x):
    def base(a):
        return a ** x

    return base


cube = pow(3)

print(cube(10))
