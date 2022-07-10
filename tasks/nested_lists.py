def sum_nestlist_recur(data):
    res = 0
    for i in range(len(data)):
        if isinstance(data[i], list):
            res += sum_nestlist_recur(data[i])
        else:
            res += data[i]
    return res


assert(sum_nestlist_recur([[1, 2, 3], [4, [5, 6]], 7])) == 28
assert(sum_nestlist_recur([[34, 56, 2, [11, 4]], [23, 11, [23, 11, [6], [5, [11, [23, [23, [4, 4]]]]]]], [23]])) == 274


def sum_nestlist_iter(data):
    pass


assert(sum_nestlist_iter([[1, 2, 3], [4, [5, 6]], 7])) == 28
assert(sum_nestlist_iter([[34, 56, 2, [11, 4]], [23, 11, [23, 11, [6], [5, [11, [23, [23, [4, 4]]]]]]], [23]])) == 274






