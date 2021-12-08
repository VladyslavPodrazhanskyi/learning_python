import requests
import multiprocessing
import time

session = None


def set_global_session():
    """
    Next we have the initializer=set_global_session
    part of that call. Remember that each process in our
    Pool has its own memory space.
    That means that they cannot share things like a Session object.
     You don’t want to create a new Session each time
     the function is called, you want to create one for each process

    """
    global session
    if not session:
        session = requests.Session()


def download_site(url):
    with session.get(url) as response:
        name = multiprocessing.current_process().name
        print(f"{name}:Read {len(response.content)} from {url}")


def download_all_sites(sites):
    with multiprocessing.Pool(initializer=set_global_session) as pool:
        pool.map(download_site, sites)


if __name__ == "__main__":
    sites = [
        "https://www.jython.org",
        "http://olympus.realpython.org/dice",
    ] * 80
    start_time = time.time()
    download_all_sites(sites)
    duration = time.time() - start_time
    print(f"Downloaded {len(sites)} in {duration} seconds")