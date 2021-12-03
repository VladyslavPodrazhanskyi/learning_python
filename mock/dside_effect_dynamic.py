import requests
import unittest
from unittest.mock import Mock

# Mock requests to control its behavior
requests = Mock()


def get_holidays():
    r = requests.get('http://localhost/api/holidays')
    if r.status_code == 200:
        return r.json()
    return None


'''
First, you created .log_request(), which takes a URL, 
logs some output using print(), then returns a Mock response. 
Next, you set the .side_effect of get() to .log_request(), 
which you’ll use when you call get_holidays(). 
When you run your test, you’ll see that get() forwards its arguments to .log_request() 
then accepts the return value and returns it as well
'''

class TestCalendar(unittest.TestCase):
    def log_request(self, url):
        # Log a fake request for test output purposes
        print(f'Making a request to {url}.')
        print('Request received!')

        response_mock = Mock()
        response_mock.status_code = 200
        response_mock.json.return_value = {
            "12/25": "Christmas",
            "7/4": "Independence Day",
        }
        return response_mock

    def test_get_holidays_logging(self):
        # Test a successful, logged request
        requests.get.side_effect = self.log_request
        assert get_holidays()['12/25'] == 'Christmas'


if __name__ == '__main__':
    unittest.main()
