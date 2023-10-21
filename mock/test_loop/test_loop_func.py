import importlib
import unittest
from unittest.mock import patch, Mock
import random

from mock.test_loop import loop_func_mod
from mock.test_loop.loop_func_mod import process

module_with_hyphen = importlib.import_module(loop_func_mod.__name__)


def f(x):
    return x ** 2 + 4


side_effect = [54, 4, 3, 1, f(5)]


class TestLoopFunc(unittest.TestCase):

    # @patch.object(module_with_hyphen, 'process', side_effect=side_effect)
    def test_loop_func(self):

        side_effect = [54, process(1), process(2), process(3), process(4)]

        with patch.object(module_with_hyphen, 'process', side_effect=side_effect):
            result = loop_func_mod.loop_func()

        self.assertEqual([54, 5, 8, 13, 20], result)


if __name__ == '__main__':
    unittest.main()

# [4, 5, 8, 13, 20]
