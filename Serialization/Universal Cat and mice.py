from pprint import pprint
import random
import json
import pickle
from ruamel.yaml import YAML
yamle = YAML()



mice_ages = list(range(1, 24))
mice_weiights = list(range(20, 200))

class Mouse:
    def __init__(self):
        self.age = random.randint(1, 24)
        self.weight = random.randint(20, 200)

def mouse_to_dict(obj):
    data = {"age": obj.age, "weight": obj.weight}
    return data

def from_dict_mouse(data):
    mouse_instance = Mouse()
    mouse_instance.age = data.get("age", random.randint(1, 24))
    mouse_instance.weight = data.get("weight", random.randint(20, 200))
    return mouse_instance


mice_list = [Mouse() for x in range(20)]
pprint(mice_list)

for mouse in mice_list:
    print(mouse.weight, mouse.age)

test_mouse = Mouse()
print(test_mouse.age, test_mouse.weight)

mouse_str = json.dumps(test_mouse, default=mouse_to_dict)
print(mouse_str)

restored_mouse = json.loads(mouse_str, object_hook=from_dict_mouse)
print(type(restored_mouse), restored_mouse.age, restored_mouse.weight)
print(restored_mouse.age == test_mouse.age and restored_mouse.weight == test_mouse.weight)

cat_names = ["Barsik", "Murzik", "Pushistik", "Sonya", "Marusya"]

class Cat:
    def __init__(self):
        self.name = random.choice(cat_names)
        self.age = random.randint(0, 22)
        self.mice = []
    def cat_mice_set(self, mice_list):
        self.mice = mice_list

my_cat = Cat()
mice_list = [Mouse() for x in range(20)]
my_cat.cat_mice_set(mice_list)
pprint(my_cat.mice)




def cat_to_dict(obj):
    data = {"name": obj.name, "age": obj.age, "mice": obj.mice}
    data["mice"] = [mouse_to_dict(mouse) for mouse in obj.mice]
    return data

def from_dict_cat(data):
    cat_instance = Cat()
    cat_instance.name = data.get("name", random.choice(cat_names))
    cat_instance.age = data.get("age", random.randint(0, 22))
    cat_instance.mice = [from_dict_mouse(mouse) for mouse in data["mice"]]
    return cat_instance

kotic = from_dict_cat({"name": "Barsik", "age": 5,
                       "mice": [{"age": 5, "weight": 40}, {"age": 12, "weight": 55}]})
print(kotic, kotic.name)
print(kotic.mice)


kotic_str = json.dumps(kotic, default=cat_to_dict)
# restored_kotic_ = json.loads(kotic_str, object_hook=from_dict_cat) # hook не работает с вложенными мышами
restored_kotic = from_dict_cat(json.loads(kotic_str))
# my_cat_str = json.dumps(my_cat, default=cat_to_dict)
# pprint(my_cat_str)
#
# # restored_cat = json.loads(my_cat_str, object_hook=from_dict_cat)
# restored_cat_dict = json.loads(my_cat_str)
# print(restored_cat_dict)
# # restore_cat = from_dict_cat(restored_cat_dict)
# # print(restore_cat, restore_cat.mice)
# print(restored_cat)
# print(restored_cat.name, my_cat.name)
# print(restored_cat.age, my_cat.age)
# pprint(restored_cat.mice)
#
# for mouse in restored_cat.mice:
#     print(type(mouse), mouse.weight, mouse.age)
