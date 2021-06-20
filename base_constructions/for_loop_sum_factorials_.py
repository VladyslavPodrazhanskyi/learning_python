def sum_fact(n):
    sum = 0
    p_fact = 1
    for i in range(1, n + 1):

    return sum

print(sum_fact(int(input())))

# developers solution with 1 loop

# n = int(input())
# partial_factorial = 1
# partial_sum = 0
# for i in range(1, n + 1):
#     partial_factorial *= i
#     partial_sum += partial_factorial
# print(partial_sum)



