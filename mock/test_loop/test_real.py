from unittest.mock import patch


class SomeClass:
    def some_method(self):
        return "Some_value"


# Create an instance of SomeClass
instance = SomeClass()


# Define the behavior you want for each call in the loop
def custom_side_effect(*args, **kwargs):
    if custom_side_effect.count == 0:
        custom_side_effect.count += 1
        return "Mocked Value"  # Mock the return value for the first call
    custom_side_effect.count = 0
    return instance.some_method()  # Return the real value for the second call


custom_side_effect.count = 0

# Mock the 'some_method' function
with patch.object(instance, 'some_method') as mock_method:
    mock_method.side_effect = custom_side_effect

    # Simulate the loop
    for _ in range(2):
        result = instance.some_method()
        print(result)

print(instance.some_method())