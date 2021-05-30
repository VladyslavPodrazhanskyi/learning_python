#Selection Sort Algorithm

def min_index(data):
    min_i = 0
    # for i in range(len(data)):
    #     if data[i] > data[max_i]:
    #         max_i = i
    # return max_i
    for i, v in enumerate(data):
        if v < data[min_i]:
            min_i = i
    return min_i


def selection_sort(data):
    selected_list = []
    while data:
        min_el = data.pop(min_index(data))
        selected_list.append(min_el)
    return selected_list



cur_data = [1, 3, 1, 120, 2, 4, 17, 16, 7, 4, 265, 11, 1, 1, 1, 1, 1, 500, 500, 500]

data = [123, 124, 23, 11, 2, 1, 4, 5]

print(selection_sort(cur_data))