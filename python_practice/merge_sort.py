def merge_sort(data):
    if len(data) < 2:
        return data[:]
    middle = int(len(data) / 2)
    left = merge_sort(data[:middle])
    right = merge_sort(data[middle:])
    return merge(left, right)


def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result


array = [78, 41, 4, 27, 3, 27, 8, 822, 19, 34, 6, 41, 13, 52, 16]

print(merge_sort(array))

#
# import operator
#
#
# def merge_sort(data, compare=operator.lt):
#     if len(data) < 2:
#         return data[:]
#     middle = int(len(data) / 2)
#     left = merge_sort(data[:middle], compare)
#     right = merge_sort(data[middle:], compare)
#     return merge(left, right, compare)
#

# def merge(left, right, compare):
#     result = []
#     i, j = 0, 0
#     while i < len(left) and j < len(right):
#         if compare(left[i], right[j]):
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1
#     while i < len(left):
#         result.append(left[i])
#         i += 1
#     while j < len(right):
#         result.append(right[j])
#         j += 1
#     return result
#
# array = [78, 41, 4, 27, 3, 27, 8, 39, 19, 34, 6, 41, 13, 52, 16]
#
# print(merge_sort(array))
