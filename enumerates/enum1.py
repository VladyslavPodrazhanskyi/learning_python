names = ['Yana', 'Peter', 'Max', 'Olga', 'Lena']

for i, name in enumerate(names):
    print('name {i} is {name}'.format(i=i, name=name))

name_index_dict = {name: index for index, name in enumerate(names)}

print(list(name_index_dict))