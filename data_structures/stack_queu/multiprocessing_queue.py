from multiprocessing import Queue

multy_queue = Queue()

multy_queue.put('apple')
multy_queue.put('plum')
multy_queue.put('pair')
multy_queue.put('banana')

print(multy_queue)

print(multy_queue.get())
print(multy_queue.get())
print(multy_queue.get())
print(multy_queue.get())
# print(multy_queue.get_nowait())
print(multy_queue.get(timeout=5))
