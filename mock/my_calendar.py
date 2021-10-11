from datetime import datetime
from unittest.mock import Mock
import requests

tuesday = datetime(year=2019, month=1, day=1)
saturday = datetime(year=2019, month=1, day=5)

datetime = Mock()


def is_weekday():
    today = datetime.today()
    # Python's datetime library treats Monday as 0 and Sunday as 6
    return (0 <= today.weekday() < 5)


# Test if today is a weekday
# assert is_weekday()


# mock .today() to return Tuesday
#
datetime.today.return_value = tuesday
assert is_weekday()
#
# # mock .today() to return Saturday

datetime.today.return_value = saturday
assert not is_weekday()







