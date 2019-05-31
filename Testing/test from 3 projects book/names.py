from name_function import get_formatted_name
print("Enter 'q' at anytime to quit")
while True:
    first = input("Input your first name or 'q' for quit: ")
    if first == "q":
        break
    last = input("Input your last name or 'q' for quit: ")
    if last == "q":
        break
    middle = input("Input your middle name or just ENTER: ")
    if middle:
        print(get_formatted_name(first, last, middle))
    else:
        print(get_formatted_name(first, last))