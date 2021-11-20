def get_board(s, l, k):
    boards = []
    for i in range(k + 1):
        boards.append(s * k + i * (l - s))
    return boards


if __name__ == '__main__':
    print(get_board(4, 5, 100))




