import json

data = {
    "int_val": 25,
    "fl_val": 25.45,
    "bool_val": False,
    "str_val": 'sfhjkfkj',
}

with open('/home/vladyslav_podrazhanskyi/projects/python/learning_python/json/data.json', 'w') as file:
    json.dump(data, file)

with open('/home/vladyslav_podrazhanskyi/projects/python/learning_python/json/data.json', 'r') as file:
    data_from_json = json.load(file)


print(data_from_json)