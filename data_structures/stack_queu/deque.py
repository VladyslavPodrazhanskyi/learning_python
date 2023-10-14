"""
The deque class implements a double-ended queue
that supports adding and removing elements
from either end in O(1) time (non-amortized).
Because deques support adding and removing elements
from either end equally well, they can serve both as queues and as stacks.

Python’s deque objects are implemented as doubly-linked lists,
which gives them excellent and consistent performance
for inserting and deleting elements but poor O(n) performance
for randomly accessing elements in the middle of a stack.
"""

from collections import deque

week_days = deque(['Mon', 'Tue', 'Wed'])

week_days.append('Thu')
week_days.appendleft('Sun')

print(week_days)  # deque(['Sun', 'Mon', 'Tue', 'Wed', 'Thu'])

print(week_days.pop())  # Thu
print(week_days.popleft())  # Sun

print(week_days)  # deque(['Mon', 'Tue', 'Wed'])
