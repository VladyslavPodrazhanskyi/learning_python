def bubble_sort(data):
    for i in range(len(data)):
        # stop_sort = True
        for k in range(len(data) - i - 1):
            if data[k] > data[k + 1]:
                data[k], data[k + 1] = data[k + 1], data[k]

        # if stop_sort:
        #     break
        print(i)
    return data


data = [4, 2, 6, -17, 1]

print(bubble_sort(data))