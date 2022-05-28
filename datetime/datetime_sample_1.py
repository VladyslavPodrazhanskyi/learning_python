from datetime import datetime
print(datetime.strptime('2021-09-01T04-00-08', '%Y-%m-%dT%H-%M-%S').date())
print(datetime.now().date())