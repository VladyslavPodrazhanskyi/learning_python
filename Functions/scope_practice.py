a = 5
b = -18

print(locals())
print(globals())

def q():
    qwert = 1
    print(locals())
    print(globals())

help(q)