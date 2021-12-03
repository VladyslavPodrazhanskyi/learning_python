import time


def generator():
    x = 1
    while True:
        yield x**3
        x += 1


g = generator()

print(g.send(None))
print(g.send(None))
print(g.send(5))

for each in g:
    time.sleep(1)
    if each <= 500:
        print(each)
    else:
        print(each)
        g.throw(Exception("each reached >= 500"))   # g.close()


