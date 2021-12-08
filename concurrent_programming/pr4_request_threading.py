import concurrent.futures
import requests
import threading
import time

thread_local = threading.local()

'''
each thread needs to create its own 
requests.Session() object
'''
def get_session():
    """
    When get_session() is called,
    the session it looks up is specific to the particular thread
    on which it’s running. So each thread will create
    a single session the first time it calls get_session()
    and then will simply use that session on each subsequent call
    throughout its lifetime.
    """
    if not hasattr(thread_local, "session"):
        thread_local.session = requests.Session()
    return thread_local.session


def download_site(url):
    session = get_session()
    with session.get(url) as response:
        print(f"Read {len(response.content)} from {url}")


"""
ThreadPoolExecutor - context manager
thread - 
pool - pool of threads, each of which can run concurrently.
executor - is the part that’s going to control 
how and when each of the threads in the pool will run. 
It will execute the request in the pool.
"""
'''
I found the fastest results somewhere 
between 5 and 10 threads. 
If you go any higher than that, 
then the extra overhead of creating and destroying the threads 
erases any time savings
'''

def download_all_sites(sites):
    with concurrent.futures.ThreadPoolExecutor(max_workers=14) as executor:  # ???
        executor.map(download_site, sites)


if __name__ == "__main__":
    sites = [
                "https://www.jython.org",
                "http://olympus.realpython.org/dice",
            ] * 80
    start_time = time.time()
    download_all_sites(sites)
    duration = time.time() - start_time
    print(f"Downloaded {len(sites)} in {duration} seconds")
