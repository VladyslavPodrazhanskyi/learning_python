import unittest
from src import average_value


class TestAverage(unittest.TestCase):
    def test_average_ints(self):
        self.assertEqual(average_value(1, 2, 3), 2)
        self.assertNotEqual(average_value(12, 4, 6), 2)

    def test_average_floats(self):
        self.assertEqual(round(average_value(1.1, 2.2, 3.6), 10), 2.3)
        self.assertNotEqual(average_value(12.5, 1.44, 3.6), 2)


if __name__ == '__main__':
    unittest.main(verbosity=2)
