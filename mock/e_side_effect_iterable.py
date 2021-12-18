"""
.side_effect can also be an iterable.
The iterable must consist of return values, exceptions,
or a mixture of both. The iterable will produce
its next value every time you call your mocked method.
For example, you can test that a retry after a Timeout returns a successful response
"""


import requests
from requests.exceptions import Timeout
import unittest
from unittest.mock import Mock

# Mock requests to control its behavior
requests = Mock()


def get_holidays():
    r = requests.get('http://localhost/api/holidays')
    if r.status_code == 200:
        return r.json()
    return None


class TestCalendar(unittest.TestCase):
    def test_get_holidays_retry(self):
        # Create a new Mock to imitate a Response
        response_mock = Mock()
        response_mock.status_code = 200
        response_mock.json.return_value = {
            '12/25': 'Christmas',
            '7/4': 'Independence Day',
        }
        # Set the side effect of requests.get()
        requests.get.side_effect = [Timeout, response_mock]
        with self.assertRaises(Timeout):
            get_holidays()
        assert get_holidays()['12/25'] == "Christmas"
        assert requests.get.call_count == 2


if __name__ == '__main__':
    unittest.main()
