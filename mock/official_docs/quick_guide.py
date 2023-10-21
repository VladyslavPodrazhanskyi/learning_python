# https://docs.python.org/3.11/library/unittest.mock.html
from unittest.mock import MagicMock

class ProductionClass:
    def method(self):
        return 5


thing = ProductionClass()
print(thing)
print(thing.method())

thing.method = MagicMock(return_value=4)
# thing.method.side_effect = [3, 1, 5, 7]



for _ in range(10):
    print(thing.method())

# thing.method.assert_called_with(1)

