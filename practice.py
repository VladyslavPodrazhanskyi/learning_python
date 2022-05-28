from dateutil.relativedelta import relativedelta

import datetime as dt

import time_machine

with time_machine.travel(dt.date(2020, 2, 29)):
    print(dt.date.today())

print(dt.date.today())
print(dt.date.today() - relativedelta(years=2))