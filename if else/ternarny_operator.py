# Example 1: Assigning a value based on a condition

x = 10
y = 20

max_value = x if x > y else y
print(max_value)  # Output: 20


# Example 2: Filtering a list

numbers = [1, 2, 3, 4, 5, 6]

even_numbers = [num for num in numbers if num % 2 == 0]
odd_numbers = [num for num in numbers if num % 2 != 0]

print(even_numbers)  # Output: [2, 4, 6]
print(odd_numbers)  # Output: [1, 3, 5]


# Example 3: Checking a condition and performing an action

age = 25

status = "Adult" if age >= 18 else "Minor"
print(status)  # Output: Adult

can_vote = True if age >= 18 else False
print(can_vote)  # Output: True


# Example 4: Assigning a default value

name = None
default_name = name if name else "Guest"
print(default_name)  # Output: Guest