x = [9, 2, 5]
y = x

y.append(6)  # mute object
y += [7]     # mute object

print(x is y) # true

y = sorted(y)  # create a new object  -  return the object
# y.sort()   - mute object, return None ( in this case x is y =  true) and both x, y - referenced to the sorted list

print(x is y) # false

print(x)   # [9, 2, 5, 6, 7]
print(y)  #  [2, 5, 6, 7, 9]
