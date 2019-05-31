# Запуск с терминала -  python -m unittest -v test_unit_culc.py
# Запуск отдельного метода
# python -m unittest -v test_unit_culc.TestCulc.test_red

import culc
import unittest


class TestCulc(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("setUP for TestCulc ")
        print("="*40)
    @classmethod
    def tearDownClass(cls):
        print("=" * 40)
        print("tearDown for TestCulc ")

    def setUp(self):
        print(f"setUp for {self.shortDescription()}")

    def tearDown(self):
        print(f"tearDown for {self.shortDescription()}")


    def test_add(self):
        """test add """
        self.assertEqual(culc.add(2, 3), 5)

    def test_red(self):
        """test red """
        self.assertEqual(culc.red(8, 3), 5)

    def test_mult(self):
        """test mult """
        self.assertEqual(culc.mult(2, 3), 6)

    def test_div(self):
        """test div """
        self.assertEqual(culc.div(15, 3), 5)







if __name__ == "__main__":

    unittest.main()