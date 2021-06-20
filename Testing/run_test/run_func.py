def run_days(first_run, record_run):
    run = first_run
    days = 1
    while run < record_run:
        run *= 1.1
        days += 1

    return days


if __name__ == '__main__':
    print(run_days(10, 20))
