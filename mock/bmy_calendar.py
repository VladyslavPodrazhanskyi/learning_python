import datetime
from unittest.mock import Mock
import requests

day = datetime.datetime(year=2019, month=1, day=1)
week_number = day.weekday()  # from 0 - Monday to 6 - Sunday
day_of_week = day.strftime('%A')


def is_weekday():
    today = datetime.datetime.today()
    return 0 <= today.weekday() < 5


assert is_weekday()  # result depends on when you run the test

# create predictable resuls with mock:

# Save a couple of test days
tuesday = datetime.datetime(year=2019, month=1, day=1)
saturday = datetime.datetime(year=2019, month=1, day=5)

datetime = Mock()
# datetime.datetime.today -  is mocked method.
# use return_value  -  to mock the method.
datetime.datetime.today.return_value = tuesday
assert is_weekday()

datetime.datetime.today.return_value = saturday
assert not is_weekday()

'''
Sometimes, you’ll want to make functions return different values 
when you call them more than once or even raise exceptions. 
You can do this using .side_effect.

side_effect defines what happens when you call the mocked function
'''
import requests


def get_holidays():
    r = requests.get('http://localhost/api/holidays')
    if r.status_code == 200:
        return r.json()
    return None

print(get_holidays())