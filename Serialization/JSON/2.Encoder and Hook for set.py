
import random
import json

test_set = {x*2 for x in range(64) if x%3 == 0}
print(f"Type: {type(test_set)}, Original set: {test_set}\n")
# json не поддерживает сериализация объектов типа set,

# поэтому для их сериализации создается специальный класс Encoder
# наследник от встроенного в модуль json класса -  json.JSONEncoder
# в этом классе прописывается только метод default, правила, по котором
# несерелизуемые объекты определенного типа должны быть превращены в серилизуемые объекты.
# Данный класс прописыввается в функции json.dumps(), как дополнительный аргумент cls=Encoder


class JsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, set):
            obj = list(obj)
            return obj



print("Test encoder and dumps for set\n")
json_str = json.dumps(test_set, cls=JsonEncoder)
print(f"type: {type(json_str)}, serialed set: {json_str}")

print("Restore set as list\n")
restored_set = json.loads(json_str)
print(f"type: {type(restored_set)}, restored set: {restored_set}")


# Тоже самое можно сделать прсто с функцией default


def default(obj):
    if isinstance(obj, set):
        obj = list(obj)
        return obj

test_set2 = {random.randint(0, 10000000) for x in range(12)}
print(f"Origin set2 typ: {type(test_set2)}, set2: {test_set2}")
print("Test encoder and dumps for set\n")
json_str2 = json.dumps(test_set2, default=default)
print(f"type: {type(json_str2)}, serialed set: {json_str2}")

print("Restore set as list\n")
restored_set2 = json.loads(json_str2)
print(f"type: {type(restored_set2)}, restored set: {restored_set2}")


# Created test_set3 and try to restore it with hook
# Unfortunately set is very complicated object and I cannot create hook to restore it.

# test_set3 = {random.randint(0, 1000) for x in range(12)}
# print(test_set3)
# print(dict(zip(list(range(len(test_set3))), [x for x in test_set3])))
#
# def default(obj):
#     data = dict(zip(list(range(len(obj))), [x for x in obj]))
#     return data
#
#
# # Для десериализации необходимо создать функцию Hook
# # def hook(data):
# #     set_instance = set()
# #     new_data = {int(k), v for k, v in data.items()}
# #     for i in range(len(new_data)):
# #         set_instance.add(new_data[i])
# #     return set_instance
#
# str_set3 = json.dumps(test_set3, default=default)
# print(str_set3, type(str_set3))
#
# restored_set3 = json.loads(str_set3, object_hook=hook)
# print(f"Type restored set {type(restored_set3)}, restored set3: {restored_set3} ")
#
#
# # restored_set3 = json.loads(str_set3)
# # print(f"Type restored set {type(restored_set3)}, restored set3: {restored_set3} ")
# #
# # # real_restore = set()
# # # print(len(restored_set3))
# # #
# # # for i in range(len(restored_set3)):
# # #     real_restore.add(restored_set3[i])
# # # print(real_restore, type(real_restore))
# #
# # a = set()
# # b = 25
# # c = {0: 12, 1: 14}
# # for i in range(len(c)):
# #     a.add(c[i])
# # print(a)
#
# a = {"0": 34, "1": 45}
# b = {int(k), v for k, v in *a.items()}

