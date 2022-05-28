"""
unittest.mock provides a powerful mechanism
for mocking objects, called patch(),
which looks up an object in a given module
and replaces that object with a Mock

patch() returns an instance of MagicMock, which is a Mock subclass.
MagicMock is useful because it implements most magic methods for you,
such as .__len__(), .__str__(), and .__iter__(), with reasonable defaults

use patch() as a decorator or a context manager
to provide a scope in which you will mock the target object.
"""

import unittest
from unittest.mock import patch
from requests.exceptions import Timeout
from g_patch import get_holidays

# A. Mock full object

# 1. patch() as a decorator
# to mock an object for the duration of your entire test function
class TestCalendarPatchDecor(unittest.TestCase):
    @patch("g_patch.requests")                                                  # mention mocking object
    def test_get_holidays_timeout_decor(self, mock_requests):                   # mention name of mocking object
        mock_requests.get.side_effect = Timeout                                 # add side effect to method of the mocking object
        with self.assertRaises(Timeout):
            get_holidays()
            mock_requests.get.assert_called_once()


# 2. patch() as a context manager
# Some reasons why you might prefer a context manager include the following:
# # You only want to mock an object for a part of the test scope.
# You are already using too many decorators or parameters, which hurts your test’s readability.

class TestCalendarPatchContextManager(unittest.TestCase):
    def test_get_holidays_timeout_cm(self):
        with patch("g_patch.requests") as mock_requests:
            mock_requests.get.side_effect = Timeout
            with self.assertRaises(Timeout):
                get_holidays()
                mock_requests.get.assert_called_once()


# B. Mock an Object’s Attributes


if __name__ == '__main__':
    unittest.main()
