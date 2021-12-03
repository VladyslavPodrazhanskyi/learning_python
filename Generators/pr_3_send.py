"""
If any input needs to be changed every time generator is called,
‘send’ method can be used to pass them.
The ‘yield’ statement returns the input passed via the ‘send’ method.

"""

def generator1():
    x = 5
    while True:
        x = yield x * 10  # don't get result (x is None now) but send it for processing with function send()


g1 = generator1()
print(next(g1)) # print(g.send(None))
print(g1.send(3))
print(g1.send(0.1))
print(g1.send(35))
print(g1.send(11))


def generator2():
    while True:
        val = yield
        yield val * 10


g2 = generator2()
print(next(g2))     # None
print(g2.send(23))  # 230
print(next(g2))     # None


def greeting_const(name):
    yield f"Hello, {name}"
    yield f"Nice to see you, {name}"
    yield f"Good morning {name}"


gc = greeting_const("Alice")

for each in gc:
    print(each)


def greeting_send(name):
    name = yield f"Hello, {name}"
    yield f"Good morning {name}"


gs = greeting_send("Alice")
print(next(gs))
print(next(gs))
# print(gs.send())


