var  =  None
my_list = var if var is not None else []
print(my_list)
var = [24, 23, 12]
my_list = var if var is not None else []
print(my_list)

my_list = [12, 134, -2, 0, 56]
for num in my_list:
    result = 1 if num >= 0 else 0
    print(result)