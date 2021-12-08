from col1.collections import deque

fifo_queue = deque()

fifo_queue.append(1)
fifo_queue.append(2)
fifo_queue.append(3)
fifo_queue.append(4)
fifo_queue.append(5)
fifo_queue.append(6)

for _ in range(len(fifo_queue)):
    print(fifo_queue.popleft())

print("*" * 80)

lifo_stack = deque()

lifo_stack.appendleft(1)
lifo_stack.appendleft(2)
lifo_stack.appendleft(3)
lifo_stack.appendleft(4)
lifo_stack.appendleft(5)
lifo_stack.appendleft(6)


for _ in range(len(lifo_stack)):
    print(lifo_stack.popleft())
