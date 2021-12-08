import asyncio
import time
import aiohttp


async def download_site(url, session):
    async with session.get(url) as response:
        # print(f"Read {len(response.content)} from {url}")  Downloaded 160 sites in 0.6768431663513184 seconds
        print(f"Read {response.content_length} from {url}") # Downloaded 160 sites in 0.8372697830200195 seconds


async def download_all_sites(sites):
    """
    The tasks can share the session because
    they are all running on the same thread

    Inside that context manager, it creates a list of tasks
    using asyncio.ensure_future()

    Once all the tasks are created,
    this function uses asyncio.gather()
    to keep the session context alive
    until all of the tasks have completed

    """
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in sites:
            task = asyncio.ensure_future(download_site(url, session))
            tasks.append(task)
        await asyncio.gather(*tasks, return_exceptions=True)


if __name__ == "__main__":

    """
    Finally, the nature of asyncio means that you have to start up the event loop 
    and tell it which tasks to run. 
    The __main__ section at the bottom of the file contains the code 
    to get_event_loop() and then run_until_complete(). 
    If nothing else, they’ve done an excellent job in naming those functions.
    """
    sites = [
        "https://www.jython.org",
        "http://olympus.realpython.org/dice",
    ] * 80
    start_time = time.time()
    asyncio.get_event_loop().run_until_complete(download_all_sites(sites))
    duration = time.time() - start_time
    print(f"Downloaded {len(sites)} sites in {duration} seconds")