import unittest


def sum_cube(first: int, second: int) -> int:
    return first ** 3 + second ** 3


class TestRunDays(unittest.TestCase):

    def test_equal(self):
        self.assertEqual(sum_cube(1, 2), 9, 'should be 9')
        self.assertEqual(sum_cube(2, 3), 35, 'should be 35')
        self.assertEqual(sum_cube(1, 10), 1001, 'should be 1001')
        self.assertEqual(sum_cube(2, 2), 16, 'should be 16')
        self.assertEqual(sum_cube(3, 3), 54, 'should be 54')

    def test_not_equal(self):
        self.assertNotEqual(sum_cube(10, 20), 100, 'should be 9000')


if __name__ == '__main__':
    unittest.main()
