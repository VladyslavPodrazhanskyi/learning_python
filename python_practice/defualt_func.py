def add_to_list(value, data=None):
    if data is None:             #  if not data:
        data = []
    data.append(value)
    return data


data_list = add_to_list('dkjf')
print(data_list)
data_list = add_to_list('dasfasfkjf', data_list)
print(data_list)
