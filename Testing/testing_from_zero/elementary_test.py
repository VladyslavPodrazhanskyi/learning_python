# 1) Without using unittest
#
# def sum(a, b):
#     return a + b
#
# def test_sum():
#     assert sum(31, 33) == 64
#     print('test passed')
#
#
# if __name__ == "__main__":
#     test_sum()

# 2) Using unittest:

import unittest

class SumTest(unittest.TestCase):

    def test_positive_nums(self):
        self.assertEqual(sum({2, 4}), 6)
    def test_negative_nums(self):
        self.assertEqual(sum([-2, -5]), -7)
    def test_mixes_nums(self):
        self.assertEqual(sum([-45, 15]), -30)
    def test_bad_type(self):
        data = ["banana", "monkey"]
        with self.assertRaises(TypeError):
            result = sum(data)





if __name__ == "__main__":
    unittest.main()

# Запуск с консоли
# python -m unittest -v elementary_test.py
# python -m unittest -v elementary_test.SumTest.test_mixes_nums
# python -m unittest - если файл начинается с test_

