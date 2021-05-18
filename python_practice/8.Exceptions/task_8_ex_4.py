def foo():
    try:
        print(1)
        return
    finally:
        print(2)
    else:
        print(3)

foo()



