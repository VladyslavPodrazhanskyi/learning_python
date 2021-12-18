'''
Sometimes, you’ll want to make functions return different values
when you call them more than once or even raise exceptions.
You can do this using .side_effect.

side_effect defines what happens when you call the mocked function
Side effect can be iterable, function, or Exception
'''

import requests
import unittest
from requests.exceptions import Timeout
from unittest.mock import Mock

# Mock requests to control its behavior
requests = Mock()


def get_holidays():
    r = requests.get('http://localhost/api/holidays')
    if r.status_code == 200:
        return r.json()
    return None


class TestCalendar(unittest.TestCase):
    def test_get_holidays_timeout(self):
        # Test a connection timeout
        requests.get.side_effect = Timeout
        with self.assertRaises(Timeout):
            get_holidays()


if __name__ == '__main__':
    unittest.main()
