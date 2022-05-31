pairs = [
    (x, y)
    for x in range(10)
    for y in [1, 2]
]

increasing_pairs = [
    (x, y)
    for x in range(10)
    for y in range(x + 1, 10)
]

print(len(pairs))  # 20
print(increasing_pairs)
print(len(increasing_pairs)) # 45
