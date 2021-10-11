def bubble_sorting(data):
    for i in range(len(data)):
        already_sorted = True
        for j in range(len(data) - i - 1):
            if data[j] > data[j + 1]:
                data[j + 1], data[j] = data[j], data[j + 1]
                already_sorted = False
        print(i)
        if already_sorted:
            break
    return data


cur_data = [1, 3, 1, 120, 2, 4, 17, 16, 7, 4, 265, 11, 1, 1, 1, 1, 1, 500, 500, 500]

data = [1, 4, 3, 12, 11, 0, -1]

print(bubble_sorting(data))


