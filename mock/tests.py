import unittest
from new_calendar import get_holidays
from requests.exceptions import Timeout
from unittest.mock import Mock, patch

"""
patch() returns an instance of MagicMock, which is a Mock subclass. 
MagicMock is useful because it implements most magic methods for you, 
such as .__len__(), .__str__(), and .__iter__(), 
with reasonable defaults.
"""


# class TestNewCalendar(unittest.TestCase):
#     @patch("new_calendar.requests")
#     def test_get_holidays_timeout(self, mock_requests):
#         mock_requests.get.side_effect = Timeout
#         with self.assertRaises(Timeout):
#             get_holidays()
#             mock_requests.get.assert_called_once()


class TestCalendar(unittest.TestCase):
    def test_get_holidays_timeout(self):
        with patch('new_calendar.requests') as mock_requests:
            mock_requests.get.side_effect = Timeout
            with self.assertRaises(Timeout):
                get_holidays()
                mock_requests.get.assert_called_once()


if __name__ == '__main__':
    unittest.main()
