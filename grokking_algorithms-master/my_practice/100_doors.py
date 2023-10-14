states = [True] * 100

for i in range(1, 101):
    for i in range(0, 100, i):
        states[i] = not states[i]


if __name__ == '__main__':
    print(states)
