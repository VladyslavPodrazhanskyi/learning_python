import importlib
import unittest
from unittest.mock import patch
import random

from mock.test_loop.loop_func import loop_func

module_with_hyphen = importlib.import_module(random.__name__)

class TestLoopFunc(unittest.TestCase):

    @patch.object(module_with_hyphen,'choice', return_value=1)
    def test_loop_func(self, rc):

        result = loop_func()

        self.assertEqual([25], result)










