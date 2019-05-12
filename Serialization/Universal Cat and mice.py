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

mouse_str = json.dumps(test_mouse, default=mouse_default)
print(mouse_str)

restored_mouse = json.loads(mouse_str, object_hook=mouse_hook)
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




def cat_default(obj):
    data = {"name": obj.name, "age": obj.age, "mice": obj.mice}
    if obj.mice:
        serialized_mice = [json.dumps(mouse, default=mouse_default) for mouse in obj.mice]
        data["mice"] = serialized_mice
    return data

def cat_hook(data):
    cat_instance = Cat()
    cat_instance.name = data.get("name", random.choice(cat_names))
    cat_instance.age = data.get("age", random.randint(0, 22))
    if data["mice"]:
        restored_mice = [json.loads(mouse, object_hook=mouse_hook) for mouse in data["mice"]]
        cat_instance.mice = restored_mice
    else:
        cat_instance.mice = []
    return cat_instance

my_cat_str = json.dumps(my_cat, default=cat_default)
pprint(my_cat_str)

restored_cat = json.loads(my_cat_str, object_hook=cat_hook)
print(restored_cat)
print(restored_cat.name, my_cat.name)
print(restored_cat.age, my_cat.age)
pprint(restored_cat.mice)

for mouse in restored_cat.mice:
    print(type(mouse), mouse.weight, mouse.age)
