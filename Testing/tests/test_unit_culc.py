# Запуск с терминала -  python -m unittest -v test_unit_culc.py
# Запуск отдельного метода
# python -m unittest -v test_unit_culc.TestCulc.test_red

import culc
import unittest


class TestCulc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(culc.add(2, 3), 5)

    def test_red(self):
        self.assertEqual(culc.red(8, 3), 5)

    def test_mult(self):
        self.assertEqual(culc.mult(2, 3), 6)

    def test_div(self):
        self.assertEqual(culc.div(15, 3), 5)

#
# if __name__ == "__main__":
#     unittest.main()
