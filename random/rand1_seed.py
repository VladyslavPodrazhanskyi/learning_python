import random

random.seed(10) # every time we receive the same result after rerun script

print(random.random())  # generate random number between 0 and 1

# generate random from range
print(random.randrange(23))
print(random.randrange(5, 23, 8))

up_to_ten = list(range(10))
random.shuffle(up_to_ten)  # shuffle list on place
for i in range(5):
    random.shuffle(up_to_ten)
    print(up_to_ten)

names = ["Inna", "Lena", "Sveta"]
print(random.choice(names))       # random member of the list

# sample without repeat
lottery_numbers = range(60)
print(random.sample(lottery_numbers, 8))

# the same with repeat:
print([random.choice(range(60)) for _ in range(8)])