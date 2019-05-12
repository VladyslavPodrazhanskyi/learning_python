file_path  = "test_file.txt"

with open(file_path) as file_object:
    lines = file_object.readlines()  # read a line in the file and save in the lest (return list of lines)

# list lines is save after close file

print(lines)

# The same code without using method readlines()

with open(file_path) as file_object:
    lines = []
    for line in file_object:
        lines.append(line)



for line in lines:
    print(line, end="")
