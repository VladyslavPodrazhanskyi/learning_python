class Apple:
    def __init__ (self, weight, taste, color, hardness):
        Apple.weight = weight
        Apple.taste = taste
        Apple.color = color
        Apple.hardness = hardness
        print('created!')

ap1 = Apple(100, 'sour','green', 'hard')
print(ap1.taste)
