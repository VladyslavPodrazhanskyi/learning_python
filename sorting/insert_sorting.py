# Insertion Sort Algorithm

def insertion_sorting(data):
    for i in range(1, len(data)):
        cur = data[i]
        j = i - 1
        while j >= 0 and data[j] > cur:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = cur
        # print(i, data)
    return data


small_data = [1, 4, 3, 12, 11, 0, -1]
cur_data = [1, 3, 1, 120, 2, 4, 17, 16, 7, 4, 265, 11]

print(insertion_sorting(small_data))
