def order_coordinates(x1, x2):
    x1, x2 = min(x1, x2), max(x1, x2)
    return x1, x2


def cross_segments(x1, x2, y1, y2):
    x1, x2 = order_coordinates(x1, x2)
    y1, y2 = order_coordinates(y1, y2)
    left, right = max(x1, y1), min(x2, y2)
    if left > right:
        return -1
    return left, right


def cross_rect(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2):
    # coordinate x
    ax1, ax2 = order_coordinates(ax1, ax2)
    bx1, bx2 = order_coordinates(bx1, bx2)
    left, right = max(ax1, bx1), min(ax2, bx2)

    # coordinate y
    ay1, ay2 = order_coordinates(ay1, ay2)
    by1, by2 = order_coordinates(by1, by2)
    low, top = max(ay1, by1), min(ay2, by2)

    if left > right or low > top:
        return False
    return True


if __name__ == '__main__':
    print(cross_segments(5, 3, 7, -1))
