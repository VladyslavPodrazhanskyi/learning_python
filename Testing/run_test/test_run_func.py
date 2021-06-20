from run_test.run_func import run_days
import unittest


class TestRunDays(unittest.TestCase):

    def test_equal(self):
        self.assertEqual(run_days(10, 20), 9, 'should be 9')
        self.assertEqual(run_days(10, 30), 13, 'should be 13')
        self.assertEqual(run_days(1, 1000), 74, 'should be 74')
        self.assertEqual(run_days(100, 101), 2, 'should be 2')
        self.assertEqual(run_days(100, 121), 3, 'should be 3')

    def test_not_equal(self):
        self.assertNotEqual(run_days(10, 20), 100, 'should be 9')

if __name__ == '__main__':
    unittest.main()
