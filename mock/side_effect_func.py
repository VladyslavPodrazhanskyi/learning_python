"""
Stable mocked value:
return_value
it ignores any arguments in when mocked function is called.

If we need different mocked values then use side_effect
and it hase priority over the return_value
(side_effect overwrites return_value)

Types of side_effect:

1) List of values ( you can result of calls of different functions there)
every next value of the list is the next result of calling mocked function
When list is OVER it raises StopIteration Exception

it ignores any arguments in when mocked function is called.

2) Custom side_effect function (can accept arguments and those arguments,
that are used to calculate returned value should be added to call mocked function.

"""


from unittest.mock import Mock


# Define a side effect function
def side_effect_func(a, b):
    if b != 0:
        return a / b
    return "ZerodivisionError"


value = 5

side_effect = [i ** 2 for i in range(2)]


# Create a mock object with the side effect function
mock_divide = Mock(return_value=value)
# mock_divide.side_effect = side_effect
# mock_divide.return_value = value
mock_divide.side_effect = side_effect_func


# Test the mock
result1 = mock_divide(20, 2)  # Returns 10
result2 = mock_divide(10, 2)  # Returns 5
result3 = mock_divide(4, 2)   # Returns 2
result4 = mock_divide(4, 2)   # Returns 2
result5 = mock_divide(4, 0)   # Returns 2
result6 = mock_divide(23, 4)   # Returns 2


print(result1, result2, result3, result4, result5)
print(result6)