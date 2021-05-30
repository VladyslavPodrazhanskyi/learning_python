def binary_search(sorted_data, value) -> int:
    if value not in sorted_data:
        return None
    start, end = 0, len(sorted_data) - 1
    while True:
        cur = (start + end) // 2
        if sorted_data[cur] > value:
            end = cur
        elif sorted_data[cur] < value:
            start = cur
        else:
            return cur



data = [i for i in range(123)]

print(binary_search(data, 151))
