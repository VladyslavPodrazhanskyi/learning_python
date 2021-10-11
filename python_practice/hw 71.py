from random import randint

"""
Develop Rectangle class with following content:
    2 private fields type of float `side_a` and `side_b` (sides А and В of the rectangle);
    One constructor with two optional parameters a and b (parameters specify rectangle sides). Side А of a rectangle
    defaults to 4, side В - 3. Raise ValueError if received parameters are less than or equal to 0;
    Method `get_side_a`, returning value of the side А;
    Method `get_side_b`, returning value of the side В;
    Method `area`, calculating and returning the area value;
    Method `perimeter`, calculating and returning the perimeter value;
    Method `is_square`, checking whether current rectangle is square or not. Returns True if the shape is square and
    False in another case;
    Method `replace_sides`, swapping rectangle sides.

Develop class ArrayRectangles, in which declare:
    Private attribute `rectangle_array` (list of rectangles);
    One constructor that creates a list of rectangles with length `n` filled with `None` and that receives an
    arbitrary amount of objects of type `Rectangle` or a list of objects of type `Rectangle` (the list must be
    unpacked inside the constructor so that there will be no nested arrays). If both objects and length are passed,
    at first creates a list with received objects and then add the required number of Nones to achieve the
    desired length. If `n` is less than the number of received objects, the length of the list will be equal to the
    number of objects;
    Method `add_rectangle` that adds a rectangle of type `Rectangle` to the array on the nearest free place and
    returning True, or returning False, if there is no free space in the array;
    Method `number_max_area`, that returns order number (index) of the first rectangle with the maximum area value
    (numeration starts from zero);
    Method `number_min_perimeter`, that returns order number (index) of the first rectangle with the minimum area value
    (numeration starts from zero);
    Method `number_square`, that returns the number of squares in the array of rectangles
"""


class Rectangle:
    def __init__(self, side_a=4.0, side_b=3.0):
        if side_a <= 0 or side_b <= 0:
            raise ValueError
        self.__a = side_a
        self.__b = side_b

    def get_side_a(self):
        return self.__a

    def get_side_b(self):
        return self.__b

    def area(self) -> float:
        return self.__a * self.__b

    def perimeter(self) -> float:
        return 2 * (self.__a + self.__b)

    def is_square(self) -> bool:
        return self.__a == self.__b

    def replace_sides(self) -> None:
        self.__a, self.__b = self.__b, self.__a

    def __repr__(self):
        return f'Rectangle: {self.__a} x {self.__b}'


class ArrayRectangles:
    def __init__(self, *args, n=0):
        self.__rectangle_array = []
        for arg in args:
            if not isinstance(arg, list):
                self.__rectangle_array.append(arg)
            else:
                for el in arg:
                    self.__rectangle_array.append(el)
        if len(self.__rectangle_array) < n:
            self.__rectangle_array += (n - len(self.__rectangle_array)) * [None]

    # def __init__(self, *args, n=0):
    #     if args:
    #         data = []
    #         for arg in args:
    #             if isinstance(arg, Rectangle):
    #                 data.append(arg)
    #             else:
    #                 for el in arg:
    #                     if isinstance(el, Rectangle):
    #                         data.append(el)
    #                     else:
    #                         for rect in el:
    #                             data.append(rect)
    #         if len(data) >= n:
    #             self.__rectangle_array = data
    #         else:
    #             self.__rectangle_array = [None] * n
    #             for i, v in enumerate(data):
    #                 self.__rectangle_array[i] = v
    #     else:
    #         self.__rectangle_array = [None] * n

    def add_rectangle(self, rect):
        if not None in self.__rectangle_array:
            return False
        self.__rectangle_array[self.__rectangle_array.index(None)] = rect
        return True

    def number_max_area(self):
        area_list = list(map(lambda rect: rect.area(), filter(lambda x: x, self.__rectangle_array)))
        max_area = max(area_list)
        return area_list.index(max_area)

    def number_min_perimeter(self):
        perimeter_list = list(map(lambda rect: rect.perimeter(), filter(lambda x: x, self.__rectangle_array)))
        min_perimeter = min(perimeter_list)
        return perimeter_list.index(min_perimeter)

    def number_square(self):
        return len(list(filter(lambda x: isinstance(x, Rectangle) and x.is_square(), self.__rectangle_array)))
