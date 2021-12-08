import asyncio


# coroutine 1

async def foo():
    print('Running in foo')
    await asyncio.sleep(0)         # make it unblocking
    print('Explicit context switch to foo again')


# coroutine 2
async def bar():
    print('Explicit context to bar')
    await asyncio.sleep(0)
    print('Implicit context switch back to bar')


ioloop = asyncio.get_event_loop()
tasks = [ioloop.create_task(foo()), ioloop.create_task(bar())]  # can be run only from other coroutine or wrapped in task create_task
# connect 2 coroutines
# coroutines task can return control back to eventloop for the next task
wait_tasks = asyncio.wait(tasks)
ioloop.run_until_complete(wait_tasks)
ioloop.close()
