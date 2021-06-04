def binary_search(data, value):
    mid = len(data) // 2
    low = 0
    high = len(data) - 1
    while data[mid] != value and low <= high:
        if value > data[mid]:
            low = mid + 1
        else:
            high = mid - 1
        mid = (low + high) // 2
    if low > high:
        return False
    return mid


data = list(range(0, 20, 2))

for el in data:
    print(binary_search(data, el))
