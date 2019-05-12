cats = "cats.txt"
dogs = "dogs.txt"

pathes = [cats, dogs]

for path in pathes:
    try:
        with open(path) as file_object:
            content = file_object.read()
        print(content+"\n")
    except FileNotFoundError:
        print(f"Sorry, but file {path} does not exist.")