import importlib
import unittest
from unittest.mock import patch, Mock
import random

from mock.test_loop.loop_func_mod import loop_func, process


class TestLoopFunc(unittest.TestCase):

    def test_loop_func(self):

        # process.side_effect = []



        result = loop_func()

        self.assertEqual([4, 5, 8, 13, 20], result)


if __name__ == '__main__':
    unittest.main()

# [4, 5, 8, 13, 20]
