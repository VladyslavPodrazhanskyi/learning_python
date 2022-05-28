from pprint import pprint
from random import randint

# https://www.digitalocean.com/community/tutorials/how-to-use-the-python-map-function-ru

# 1) map(function, eterable)
# Объект map -  является итератором.
# 1.1 map with lambda:  map(lambda item: item[] expression, iterable)

# numbers = [10, 15, 21, 33, 42, 55]
numbers = [10]

mapped_numbers = list(map(lambda x: x + x * 3, numbers))
print(mapped_numbers)

##################################################################


names = ['Vlad', 'Lena', 'Igor', 'Nick', 'Olga', 'John', 'Ann']
ages = [randint(5, 75) for _ in range(7)]



people = [{'name': names[i], 'age': ages[i]} for i in range(len(names))]
# people = [{'age': 53, 'name': 'Vlad'},
#     {'age': 9, 'name': 'Lena'},
#     {'age': 59, 'name': 'Igor'},
#     {'age': 14, 'name': 'Nick'},
#     {'age': 26, 'name': 'Olga'},
#     {'age': 16, 'name': 'John'},
#     {'age': 48, 'name': 'Ann'}]

sum_ages = sum(map(lambda d: d.get('age', 0), people))
names_from_map = list(map(lambda d: d.get('name'), people))

print(sum_ages)
print(names_from_map)
print(names_from_map == names)


# 1.2. map with custom function:

aquarium_creatures = [
    {"name": "sammy", "species": "shark", "tank number": 11, "type": "fish"},
    {"name": "ashley", "species": "crab", "tank number": 25, "type": "shellfish"},
    {"name": "jo", "species": "guppy", "tank number": 18, "type": "fish"},
    {"name": "jackie", "species": "lobster", "tank number": 21, "type": "shellfish"},
    {"name": "charlie", "species": "clownfish", "tank number": 12, "type": "fish"},
    {"name": "olly", "species": "green turtle", "tank number": 34, "type": "turtle"}
]

tank_number = 42

def asign_tank_number(aquarium_creatures, new_tank_number):
    def apply(x):
        x["tank number"] = new_tank_number
        return x
    return map(apply, aquarium_creatures)

print(list(asign_tank_number(aquarium_creatures, 142)))

# Использование встроенной функции с несколькими итерируемыми объектами.
# map() продолжит обрабатывать несколько итерируемых объектов,
# пока не достигнет конца объекта, содержащего меньше всего элементов.

print(pow(4, 5))   # 4**5

base_numbers = list(range(5))
powers = list(range(8))

for el in map(pow, base_numbers, powers):
    print(el, end=', ')
print('\n')


# 2) reduce(function, eterable):

from functools import reduce


def quarter_sum(a, b):
    return (a + b) / 4


def double_sum(a, b):
    return (a + b) * 2


print(numbers)  # numbers = [10, 15, 21, 33, 42, 55]
print(reduce(quarter_sum, numbers))
print(reduce(lambda a, b: (a + b) / 4, numbers))
print(reduce(double_sum, numbers))
print(reduce(lambda a, b: (a + b) * 2, numbers))

# 3. filter:
data = [randint(-100, 100) for _ in range(25)]
selected_data = [el for el in data if abs(el) <= 35]

filtered_data = filter(lambda x: abs(x) <= 35, data)

print(data)
print(selected_data)
print(list(filtered_data))
print(selected_data == list(filtered_data))  # false ????

# all()    -  последовательность логич И в итераторе.
conditions_all_true = [True, 1, 65, {'d', 4}]
conditions_part_true = [True, False, 1, [], {'d', 4}]
conditions_all_false = [False, [], False, {}, '']

print(all(conditions_all_true))
print(all(conditions_part_true))
print(all(conditions_all_false))


# any - последовательность логич ИЛИ в итераторе.

print(any(conditions_all_true))
print(any(conditions_part_true))
print(any(conditions_all_false))