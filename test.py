def is_queen_beat(x1, y1, x2, y2):
    if x1 == x2 or y1 == y2 or abs(x1 - x2) == abs(y1 - y2):
        return True
    return False


list_data = []
flag = False

for i in range(8):
    x, y = [int(el) for el in input().split()]
    list_data.append((x, y))

for i in range(len(list_data) - 1):
    for j in range(i + 1, len(list_data)):
        if is_queen_beat(*list_data[i], *list_data[j]):
            flag = True
            break

if flag:
    print('YES')
else:
    print('NO')





