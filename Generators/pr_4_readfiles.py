with open("log.txt", "r") as log_file:
    log_list = [st for st in log_file]
    log_gen = (st for st in log_file)


def reader(filename):
    with open(filename, "r") as file:
        for line in file:
            yield line


reader_log_txt = reader("log.txt")
for i in range(10):
    print(next(reader_log_txt))

reader_gen = reader("log.txt")

total_rows = 0
error_rows = 0

for row in reader_gen:
    total_rows += 1
    if "error" in row:
        error_rows += 1


print(total_rows)
print(error_rows)