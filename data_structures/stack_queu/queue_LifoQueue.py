"""
queue.LifoQueue: Locking Semantics for Parallel Computing
The LifoQueue stack implementation in the Python standard library
is synchronized and provides locking semantics
to support multiple concurrent producers and consumers.

Besides LifoQueue, the queue module contains several other classes
that implement multi-producer, multi-consumer queues that are useful
for parallel computing.

Depending on your use case,
the locking semantics might be helpful,
or they might just incur unneeded overhead.
In this case, you’d be better off using a list or a deque as a general-purpose stack

"""

from queue import LifoQueue

my_stack = LifoQueue()
my_stack.put('apple')
my_stack.put('strawberry')
my_stack.put('plum')
my_stack.put('pair')

print(my_stack)
print(type(my_stack))

print(my_stack.get())
print(my_stack.get_nowait())
print(my_stack.get())
print(my_stack.get_nowait())
# print(my_stack.get(timeout=5))
print(my_stack.get_nowait())

