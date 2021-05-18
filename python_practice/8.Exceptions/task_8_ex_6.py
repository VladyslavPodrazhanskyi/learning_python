flag = False
while not flag:
    try:
        filename = input("Enter filename: ")
        with open(filename, 'r') as file:
            print(file.read())
    except:
        print("Input file not found")
