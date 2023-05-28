import time


def control_calls(limit, calls):
    quantity_requests = 0
    start_time = time.monotonic()
    for i in range(calls):
        print(i)
        quantity_requests += 1

        end_time = time.monotonic() - start_time

        while quantity_requests >= limit:
            if end_time <= 1:
                time.sleep(0.01)
            else:
                start_time = time.monotonic()
                quantity_requests = 0
            end_time = time.monotonic() - start_time


if __name__ == '__main__':

    start_time = time.monotonic()
    print('start_time', start_time)
    control_calls(10, 1000)
    print('end_time', time.monotonic() - start_time)
