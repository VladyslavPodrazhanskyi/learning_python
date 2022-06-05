def if_even(n: int) -> bool:
    if n < 2:
        return not bool(n)
    return if_even(n - 2)


print(if_even(123))
print(if_even(124))
