import json

user_name = input("Dear User, please input your name: ")



file_path = "name.json"

with open(file_path, "w") as file_object:
    json.dump(user_name, file_object)

with open(file_path) as file_object:
    remember_name = f"Hi, {json.load(file_object)}! I remember your name."

print(remember_name)