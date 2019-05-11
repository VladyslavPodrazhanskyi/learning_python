import json

separator = "+"*25 + "\n"*2 + "+"*25

DATA = {"int": 5,
        "float": 34.53,
        "tuple": ("qwweqw", 392, "fehke"),  # tuple серилизуется в list
        "list": [x**3 for x in range(4)],
        "dict": {"month": "october", "year": 1953},
        }

del DATA["tuple"]
# DATA["set"] = {x*45 for x in range(25) if x%5 == 0}

print("Выводим исходный словарь DATA")

for k, v in DATA.items():
    print(f"key: {k}, v: {v}, type: {type(v)}")

print(separator)

print("Testing dumps")
formatted_str = json.dumps(DATA)
print(f"formatted_str: {formatted_str}")

print(separator)

print("Testing eval")
eval_restored_DATA = eval(formatted_str)
print(f"Type of eval_restored_DATA: {type(eval_restored_DATA)}")
for k, v in eval_restored_DATA.items():
    print(f"key: {k}, v: {v}, type: {type(v)}")

print(separator)

print("Testing loads")
loads_restored_DATA = json.loads(formatted_str)
type(loads_restored_DATA)
for k, v in loads_restored_DATA.items():
    print(f"key: {k}, v: {v}, type: {type(v)}")

print(separator)

print("Testing correction of serialization")
print(DATA == eval_restored_DATA)  # false as tuple was dumped in list, True if tuple is deleted from DATA
print(DATA ==  loads_restored_DATA)  # false as tuple was dumped in list, True if tuple is deleted from DATA
print(eval_restored_DATA == loads_restored_DATA) # true

print(separator)
print("Testing dump and load")

path = "JsonDATA.json"
with open(path, "w") as file:
    json.dump(DATA, file)
print("JsonDATA.json file was created")
print("Read conten of this file")
with open(path) as file:
    content = file.read()
print(f"Content of json file: {content}")

print(separator)
print("Restore object from jsonfile ")
with open(path) as file:
    load_restored_DATA = json.load(file)

for k, v in load_restored_DATA.items():
    print(f"key: {k}, v: {v}, type: {type(v)}")