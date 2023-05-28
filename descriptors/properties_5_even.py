
# using property decorator
class Even:
    def __init__(self):
        self._value = 0

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, val):
        self._value = val if val % 2 == 0 else 0


even = Even()

print(even.value)

even.value = 23
print(even.value)

even.value = 4
print(even.value)

even.value = 23
print(even.value)

