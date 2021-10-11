"""
Пете нужно оклеить обоями стену размером N метров в высоту и M метров в ширину.
Для поклейки используются обои, которые продаются рулонами.
Каждый рулон имеет ширину 1 метр и длину K метров.
 Обои клеятся на стену вертикальными полосами (сверху вниз).
 При этом Петя хочет так поклеить обои, чтобы горизонтальных стыков разных кусков не было
 (то есть один цельный кусок клеится от потолка до пола).
 От рулона можно отрезать куски нужного размера
 (иногда при этом может оставаться кусок, меньшего размера,
 который поэтому не может быть поклеен, этот кусок идет в отходы).
По данным числам N, M и K определите наименьшее количество рулонов,
которое нужно купить Пете, чтобы оклеить всю стену.

Входные данные
Вводятся натуральные числа N, M и K (1 ≤ N ≤ 100, 1 ≤ M ≤ 100, N ≤K ≤100).

Выходные данные
Выведите одно число - количество рулонов, которые должен купить Петя.
"""


def wallpaper(n, m, k):
    mr = k // n
    return (m + mr - 1) // mr  # m / mr  -  with round up


if __name__ == '__main__':
   print(wallpaper(3, 6, 9))
