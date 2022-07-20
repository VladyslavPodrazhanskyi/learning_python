# Запуск с терминала -  python -m unittest -v test_unit_culc.py
# Запуск отдельного метода
# python -m unittest -v test_unit_culc.TestCulc.test_red

import unittest
from Testing.tests.culc import add, red, mult, div


class TestCulc(unittest.TestCase):

    @classmethod  # запускается вначале тестирования данного класса
    def setUpClass(cls):
        print("setUP for TestCulc ")
        print("=" * 40)

    @classmethod  # Запускается в конце тестирования данного класса
    def tearDownClass(cls):
        print("=" * 40)
        print("tearDown for TestCulc ")

    def setUp(self):  # запускается вначале тестирования каждого метода данного класса
        print(f"setUp for {self.shortDescription()}")

    def tearDown(self):  # запускается в конце тестирования каждого метода данного класса
        print(f"tearDown for {self.shortDescription()}")

    def test_add(self):
        """test add """
        self.assertEqual(add(2, 3), 5)

    def test_red(self):
        """test red """
        self.assertEqual(red(8, 3), 5)

    def test_mult(self):
        """test mult """
        self.assertEqual(mult(2, 3), 6)

    def test_div(self):
        """test div """
        self.assertEqual(div(15, 3), 5)


if __name__ == "__main__":
    unittest.main()
