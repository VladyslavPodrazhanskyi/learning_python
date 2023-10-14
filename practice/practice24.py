from datetime import datetime, timedelta

# Assuming last_ingested_date_str contains the date string '20231002' (for example)
last_ingested_date_str = '20200403'

# Parse the date string into a datetime object
ingested_date = datetime.strptime(last_ingested_date_str, '%Y%m%d')

print('ingested_date')
print(ingested_date)

# Replace the day component with 1
first = ingested_date.replace(day=1)
print("first")
print(first)

last_month = first - timedelta(days=1)
print("last_month")
print(last_month)
print(type(last_month))






