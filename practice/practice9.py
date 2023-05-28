from datetime import datetime, timedelta

history_start_date = datetime.now() - timedelta(days=30)
datetime_str = '09/19/21'
new_history_start_date = datetime.strptime(datetime_str, '%m/%d/%y')

print(history_start_date)
print(type(new_history_start_date))
print(new_history_start_date)