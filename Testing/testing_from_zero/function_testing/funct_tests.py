import unittest

from function_testing.for_testing import random_list


class ListTest(unittest.TestCase):
    def setUp(self):
        self.test_list = random_list()

    def tearDown(self):
        print(self.test_list)

    def test_type(self):
        self.assertIsInstance(self.test_list, list)

    def test_len(self):
        self.assertEqual(len(self.test_list), 20)

    def test_el_type(self):
        for el in self.test_list:
            self.assertIsInstance(el, int)

    def test_el_number(self):
        for el in self.test_list:
            self.assertIn(el, range(0, 101))


if __name__ == "__main__":
    unittest.main()