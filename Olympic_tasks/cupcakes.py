"""
Для праздничного чаепития необходимо купить n пирожных.
В магазине продается всего два вида пирожных,
причем пирожных одного вида осталось a штук, а пирожных другого вида осталось b штук.
Пирожные одного вида считаются одинаковыми.
Сколькими способами можно купить ровно n пирожных?
"""


n = int(input())
a = int(input())
b = int(input())
full_count = 0
count = 0
# for i in range(min(a, n) + 1):
#     for j in range(min(b, n) + 1):
#         if i + j == n:
#             count += 1
#         full_count += 1


for i in range(a + 1):
    if 0 < n - i <= b:
        count += 1
    full_count += 1

print(count)
print(full_count)
