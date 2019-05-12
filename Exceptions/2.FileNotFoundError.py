file_path = "Alice.txt"

# with open(file_path, "w") as file_object:
#     file_object.write("Alice is the most beautiful princess.")

try:
    with open(file_path) as file_object:
        contents = file_object.read()
        print(contents)

except FileNotFoundError:
    print(f"Sorry, but file {file_path} does NOT exist.")

