x = 'global'
def outer():
    # x = 'nonlocal'
    def inner():
        # x = 'local'
        return x
    return inner()

print(outer())

#
#
# from pprint import pprint
# from random import randint
#
# x = 'global'
#
# def outer_func():
#     x = 394832
#     def inner_func():
#         nonlocal x
#         x = 'non local from inner'
#     inner_func()
#     return x
#
# print(outer_func())
#
#
# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
# d1 = Dog('Buity', 7)
#
#
# pprint(dir())