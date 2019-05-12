from ruamel.yaml import YAML
yaml = YAML()
from pprint import pprint
import random
mice_ages = list(range(1, 24))
mice_weiights = list(range(20, 200))

class Mouse:
    def __init__(self):
        self.age = random.randint(1, 24)
        self.weight = random.randint(20, 200)

    def __str__(self):
        return f"Mouse. age: {self.age}. Weight :{self.weight}"

# # setstate and getstate сейчас установлены по дефолту и никак не воздействуют на код.
#
# # getstat используется для сериализации (принимает объект, возвращает словарь с параметрами
#     def __getstate__(self):
#                               # здесь можно менять любые параметры словаря
#         return self.__dict__
# # setstate испльзуется для десериализации.
#
#     def __setstate__(self, state):    # принимает словарь , возвращает состояние объекта
#         self.__dict__ = state        # сюда можно внести код, кот изменит объект при дессириализации.


test_mouse = Mouse()
print(test_mouse)



# mouse_str = yaml.dumps(test_mouse)
# print(mouse_str)
#
# restored_mouse = yaml.loads(mouse_str)
# print(type(restored_mouse), restored_mouse.age, restored_mouse.weight)
# print(restored_mouse.age == test_mouse.age and restored_mouse.weight == test_mouse.weight)

with open("test_mouse.yaml", "w") as file:
    yaml.dump(test_mouse, file)
with open("test_mouse.yaml") as file:
    mouse_from_file = yaml.load(file)
print(mouse_from_file)


mice_list = [Mouse() for x in range(20)]
pprint(mice_list)

for mouse in mice_list:
    print(mouse)





# cat_names = ["Barsik", "Murzik", "Pushistik", "Sonya", "Marusya"]
#
# class Cat:
#     def __init__(self):
#         self.name = random.choice(cat_names)
#         self.age = random.randint(0, 22)
#         self.mice = []
#     def cat_mice_set(self, mice_list):
#         self.mice = mice_list
#
# # setstate and getstate сейчас установлены по дефолту и никак не воздействуют на код.
# # setstate испльзуется для десериализации.
#     def __setstate__(self, state):    # принимает словарь , возвращает состояние объекта
#         self.__dict__ = state
#
# # getstat используется для сериализации (принимает объект, возвращает словарь с параметрами
#     def __getstate__(self):
#         return self.__dict__
#
#
#
#
#
# my_cat = Cat()
# mice_list = [Mouse() for x in range(20)]
# my_cat.cat_mice_set(mice_list)
# pprint(my_cat.mice)
#
#
#
#
# # def cat_default(obj):
# #     data = {"name": obj.name, "age": obj.age, "mice": obj.mice}
# #     if obj.mice:
# #         serialized_mice = [json.dumps(mouse, default=mouse_default) for mouse in obj.mice]
# #         data["mice"] = serialized_mice
# #     return data
# #
# # def cat_hook(data):
# #     cat_instance = Cat()
# #     cat_instance.name = data.get("name", random.choice(cat_names))
# #     cat_instance.age = data.get("age", random.randint(0, 22))
# #     if data["mice"]:
# #         restored_mice = [json.loads(mouse, object_hook=mouse_hook) for mouse in data["mice"]]
# #         cat_instance.mice = restored_mice
# #     else:
# #         cat_instance.mice = []
# #     return cat_instance
#
# my_cat_str = pickle.dumps(my_cat)
# pprint(my_cat_str)
#
# restored_cat = pickle.loads(my_cat_str)
# print(restored_cat)
# print(restored_cat.name, my_cat.name)
# print(restored_cat.age, my_cat.age)
# pprint(restored_cat.mice)
#
# print("Мышки восстановленного кота")
# for mouse in restored_cat.mice:
#     print(type(mouse), mouse.weight, mouse.age)
#
#  # def garage_info(self):
#  #        garages_info = {'Town': self.town, 'Place': self.places, 'Owner': self.owner, 'Cars': [car.car_info() for car in self.cars.values()]}
#  #        return garages_info
#
# # @classmethod
# #     def to_yaml(cls, representer, node):
# #         return representer.represent_scalar(cls.yaml_tag, u'{.town}_{.cars}_{.places}_{.owner}'
# #                                             .format(node, node, node, node))
# #
# #     @classmethod
# #     def from_yaml(cls, constructor, node):
# #         return cls(*node.value.split('_'))