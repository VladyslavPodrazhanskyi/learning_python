file_path1  = "guest.txt"
guest_name = input('Input your name, please: ')

with open(file_path1, "w") as file_object:
    file_object.write(f"Your name is {guest_name}!")


file_path2 = "guests_book.txt"

with open(file_path2, "a") as file_object:
    while True:
        guest_name = input('Input your name, please: ')
        if guest_name == "q":
            break
        message = f"Hello, {guest_name}. It's nice to see you in our Hotel!\n"
        file_object.write(message)
