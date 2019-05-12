cats = "cats.txt"
dogs = "dogs.txt"

with open(cats, "w") as f_object:
    f_object.write("Barsik,\nMurzik,\nMurlyka")

with open(dogs, "w") as f_object:
    f_object.write("Barbos,\nTobik\nAgbar")

with open(cats) as f_object:
    content = f_object.read()

print(content)

with open(dogs) as f_object:
    content = f_object.read()

print(content)