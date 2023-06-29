from collections import deque

week_days = deque(['Mon', 'Tue', 'Wed'])

week_days.append('Thu')
week_days.appendleft('Sun')

print(week_days)  # deque(['Sun', 'Mon', 'Tue', 'Wed', 'Thu'])

print(week_days.pop())  # Thu
print(week_days.popleft())  # Sun

print(week_days)  # deque(['Mon', 'Tue', 'Wed'])
