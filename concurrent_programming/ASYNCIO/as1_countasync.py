"""
As you’ll see in the next section,
the benefit of awaiting something, including asyncio.sleep(),
is that the surrounding function can temporarily code control
to another function that’s more readily able to do something immediately.
 In contrast, time.sleep() or any other blocking call is incompatible
 with asynchronous Python code, because it will stop everything
 in its tracks for the duration of the sleep time.
"""

import asyncio


async def count():
    """
    The syntax async def introduces either a native coroutine
    or an asynchronous generator ( if use yield).
    """
    print("One")
    await asyncio.sleep(1) # make it unblocking allows the task to hand control back to the event loop
    print("Two")


async def main():
    await asyncio.gather(count(), count(), count())


if __name__ == "__main__":
    import time

    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")
