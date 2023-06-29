from utils import is_hashable


class Apple:
    def __init__(self, color, weight):
        self.color = color
        self.weight = weight


apple = Apple('green', 110)

apple_dict = {
    apple: 'my_apple'
}

print(apple_dict)
print(hash(apple))


data = [1, 34, 'we']

print(is_hashable(apple))
print(is_hashable(data))
