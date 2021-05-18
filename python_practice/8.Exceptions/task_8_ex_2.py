def foo():
    try:
        bar(x, 4)
    finally:
        print('after bar')
    print('or this after bar?')


foo()
