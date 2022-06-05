'''
https://pythonist.ru/rekursivnye-funkczii-v-python/
'''


def pn(num: int) -> None:
    if num >= 1:
        pn(num - 1)
        print(num)


pn(3)
