def quick_sort(data):
    if len(data) < 2:
        return data
    pivot = data[0]
    less_eq = [el for el in data[1:] if el <= pivot]
    greater = [el for el in data[1:] if el > pivot]
    return quick_sort(less_eq) + [pivot] + quick_sort(greater)


data = [1, 4, 3, 12, 11, 0, -1]

print(quick_sort(data))



# def rec_bin_search(sort_data, value):
#     if
#
#
#
#
# data = [12, 15, 56, 64, 1156]
#
#
# print(rec_bin_search(data, 56))



