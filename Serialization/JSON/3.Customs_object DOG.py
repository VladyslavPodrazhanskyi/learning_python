import json

test_set = {"set": {x*2 for x in range(64) if x%3 == 0}}
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

# Для десериализации необходимо создать функцию Hook,


def hook(obj):
    if "set" in obj:
        return set(obj)





print("Test encoder and dumps for set")
json_str = json.dumps(test_set, cls=JsonEncoder)
print(json_str)

restored_set = json.loads(json_str, object_hook=hook)
print(restored_set)