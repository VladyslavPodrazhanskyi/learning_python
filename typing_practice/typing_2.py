"""
https://realpython.com/python-type-checking/#example-a-deck-of-cards
"""
def double(number: int) -> int:
    return number * 2

print(double(True))  # Passing in bool instead of int