from time import monotonic

start_time = monotonic()
for i in range(10000000):
    print(i)
end_time = monotonic()
print(end_time - start_time)
# 26.165216897963546
# start_time = monotonic()
# i = 0
# while i < 10000000:
#     print(i)
#     i += 1
# end_time = monotonic()
# print(end_time - start_time)
# 23.778636825969443
