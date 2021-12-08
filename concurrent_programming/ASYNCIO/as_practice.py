import asyncio


async def func_one():
    print("func_one starts")
    await asyncio.sleep(2)
    print("func_one finished")


async def func_two():
    print("func_two starts")
    await asyncio.sleep(2)
    print("func_two finished")


async def main():
    await asyncio.gather(func_one(), func_two())


if __name__ == '__main__':
    asyncio.run(main())

