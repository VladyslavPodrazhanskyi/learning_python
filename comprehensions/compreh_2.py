from random import randint

numbers = [randint(-20, 20) for x in range(8)]
square_numbers = [{x: x**2} for x in numbers if abs(x) <= 10]
if_else_square_numbers = [{x: -x**2} if x > 0 else {x: x**2} for x in numbers if abs(x) <= 10]

print(numbers)
print(square_numbers)
print(if_else_square_numbers)
