import unittest
from calculator import Calculator
from unittest.mock import patch


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_summ(self):
        answer = self.calc.summ(2, 4)
        self.assertEqual(answer, 6)


class TestCacWithMock(unittest.TestCase):
    @patch('calculator.Calculator.summ', return_value=9)
    def test_summ(self, summ):
        self.assertEqual(summ(2, 8), 9)


if __name__ == '__main__':
    unittest.main()
