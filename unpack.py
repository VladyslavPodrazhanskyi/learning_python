"""
 The * prefix operator operates in two directions:
1)  when using it in a function,
it unpacks the argument so it looks like it was individually passed.
2) Used in a function definition,
it packs all the arguments of the function call into a tuple

"""
# * in def of functions:

# Using *args in a function definition.
# Every argument after the first gets lumped into a
# tuple named cols.


def sum_args(*args: int) -> int:
    return sum(args)


print(sum_args(34, 234, 242, 242))


# * in functions:

# without * we add only 1 arg -  list and receive type error
# print(sum_args([34, 234, 242, 242]))  # type error

# with * we add several arguments to the function
print(sum_args(*[34, 234, 242, 242]))
