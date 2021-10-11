def gen(x):
    while True:
        x = (yield x) + 1





my_gen = gen(20)
print(my_gen.send(None))  # print(next(my_gen))
print(my_gen.send(15))
print(my_gen.send(18))
print(my_gen.send(-7))


#
# def count(start=0, stop=10, step=1):
#     num = start
#     while num < stop:
#         val = yield num
#         if val is not None:
#             num = val
#         num += step
#
#
# my_count = count(stop=20)
#
# for item in my_count:
#     print(item)
#     if item > 7:
#         my_count.send(14)

