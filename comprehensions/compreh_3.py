# списковое включение, выдаёт [2, 3, 4]
l1 = [x + 1 for x in (1, 2, 3)]

# генераторное выражение, выдаст 2, затем 3, затем 4
g1 = (x + 1 for x in (1, 2, 3))

# списковое включение с фильтром выдаёт [2]
l2 = [x for x in (1, 2, 3) if x % 2 == 0]

# списковое включение с тройкой [1, 3, 3]
l3 = [x + 1 if x % 2 == 0 else x for x in (1, 2, 3)]

# списковое включение с тройкой и фильтрацией [1, 3, 3]
l4 = [x + 1 if x % 2 == 0 else x for x in range(-3, 4) if x > 0]

# множество выражений, выдаёт {1, 2, 3}
s1 = {x for x in (1, 2, 2, 3)}

# словарь включений, выдаёт {'a': 1, 'b': 2} (python 2.7+ and 3.0+ only)
d1 = {k: v for k, v in [('a', 1), ('b', 2)]}

# Вложенные циклы, дает [11, 21, 12, 22]
l5 = [x + y for x in [1, 2] for y in [10, 20]]

# Состояние проверено на 1-й петле [6, 7, 8]
l6 = [x + y for x in [1, 2, 3] if x > 2 for y in [3, 4, 5]]

# Состояние проверено на 2-й петле [5, 6, 6, 7, 7, 8]
l7 = [x + y for x in [1, 2, 3] for y in [3, 4, 5] if y > 3]
