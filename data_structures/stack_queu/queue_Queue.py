"""
The queue.Queue implementation in the Python standard library
is synchronized and provides locking semantics
to support multiple concurrent producers and consumers.

The queue module contains several other classes implementing multi-producer,
multi-consumer queues that are useful for parallel computing.

Depending on your use case, the locking semantics might be helpful
or just incur unneeded overhead. In this case,
you’d be better off using collections.deque as a general-purpose queue
"""

from queue import Queue

my_queue = Queue()
my_queue.put('apple')
my_queue.put('strawberry')
my_queue.put('plum')
my_queue.put('pair')

print(my_queue)
print(type(my_queue))

print(my_queue.get())
print(my_queue.get_nowait())
print(my_queue.get())
print(my_queue.get_nowait())
# print(my_queue.get(timeout=5))
print(my_queue.get_nowait())

