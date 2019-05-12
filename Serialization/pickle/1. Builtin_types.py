import pickle

separator = "+"*25 + "\n"*2 + "+"*25

DATA = {"int": 5,
        "float": 34.53,
        "tuple": ("qwweqw", 392, "fehke"),  # tuple серилизуется в list
        "list": [x**3 for x in range(4)],
        "dict": {"month": "october", "year": 1953},
        "set": {x**3 for x in range(49) if x%7 == 1}
        }


print("Выводим исходный словарь DATA")

for k, v in DATA.items():
    print(f"key: {k}, v: {v}, type: {type(v)}")

print(separator)

print("Testing dumps")
formatted_str = pickle.dumps(DATA)
print(f"formatted_str: {formatted_str}")

print(separator)

print("Testing eval")
# eval_restored_DATA = eval(formatted_str)
# print(f"Type of eval_restored_DATA: {type(eval_restored_DATA)}")
# for k, v in eval_restored_DATA.items():
#     print(f"key: {k}, v: {v}, type: {type(v)}")
#
print("Eval does not work with pickle")
print(separator)



print("Testing loads")
loads_restored_DATA = pickle.loads(formatted_str)
type(loads_restored_DATA)
for k, v in loads_restored_DATA.items():
    print(f"key: {k}, v: {v}, type: {type(v)}")

print(separator)

print("Testing correction of serialization")

print(DATA ==  loads_restored_DATA)

print(separator)
print("Testing dump and load")

path = "pickleDATA.txt"
with open(path, "w") as file:
    pickle.dump(DATA, file)
print("pickleDATA.txt file was created")
print("Read conten of this file")
with open(path) as file:
    content = file.read()
print(f"Content of pickle file: {content}")

print(separator)
print("Restore object from picklefile ")
with open(path) as file:
    load_restored_DATA = pickle.load(file)

for k, v in load_restored_DATA.items():
    print(f"key: {k}, v: {v}, type: {type(v)}")