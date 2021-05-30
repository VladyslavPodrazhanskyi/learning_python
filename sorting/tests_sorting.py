import unittest

from sorting.bubble_sorting import bubble_sorting
from sorting.insert_sorting import insertion_sorting

cur_data = [1, 3, 1, 120, 2, 4, 17, 16, 7, 4, 265, 11]


def test_bubble():
    assert bubble_sorting(cur_data) == sorted(cur_data)


def test_insertion():
    assert insertion_sorting(cur_data) == sorted(cur_data)


class TestSorting(unittest.TestCase):
    def test_bubble_sorting(self):
        self.assertEqual(sorted(cur_data), bubble_sorting(cur_data))

    def test_insertion_sorting(self):
        self.assertEqual(sorted(cur_data), insertion_sorting(cur_data))
