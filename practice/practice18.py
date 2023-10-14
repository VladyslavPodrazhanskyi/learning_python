import re

line = "skfj [time date] slfjsk"

print(line.split('[')[1].split(']')[0])
# print(line.split()[3].strip('[]'))
# print(" ".join(line.split("[" or "]")[3:5]))
# print(" ".join(line.split()[3:5]).strip("[]"))
print(re.split("\[|\]", line)[1])