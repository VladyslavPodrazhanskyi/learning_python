"""
You can set .return_value and .side_effect on a Mock directly.
However, because a Python mock object needs to be flexible
 in creating its attributes, there is a better way to configure
 these and other settings.
"""
from unittest.mock import Mock

# 1. configure a Mock by specifying certain attributes
# when you initialize an object
mock_return_value = Mock(return_value=56)
print(mock_return_value()) # 56

mock_side_effect_func = Mock(side_effect=lambda x: x ** 2)
print(mock_side_effect_func(5)) # 25

mock_side_effect_iter = Mock(side_effect=[1, 2, 3])
for _ in range(3):
    print(mock_side_effect_iter())  # 1, 2, 3  if 4 then StopIteration

mock_side_effect_exception = Mock(side_effect=Exception)


"""
While .side_effect and .return_value 
can be set on the Mock instance, itself, 
other attributes like .name 
can only be set through .__init__() or .configure_mock(). 
"""
mock_config_name = Mock(name="Funny mock")
print(mock_config_name) # <Mock name='Funny mock' id='139824006334208'>
print(mock_config_name.name) # <Mock name='Funny mock.name' id='139764876938400'>

"""
f you access mock.name you will create a .name attribute 
instead of configuring your mock.
"""

mock = Mock()
mock.name = "Funny mock"
print(mock.name)   # Funny mock

# 2. configure an existing Mock
# using .configure_mock()

mock = Mock()
mock.configure_mock(return_value=125)
print(mock())

"""
3. Unpacking a dictionary into either .configure_mock() or Mock.__init__(), 
you can even configure your Python mock object’s attributes.
"""

# Verbose, old Mock
response_mock = Mock()
response_mock.json.return_value = {
    '12/25': 'Christmas',
    '7/4': 'Independence Day',
}

# Shiny, new .configure_mock()
holidays = {'12/25': 'Christmas', '7/4': 'Independence Day'}
response_mock = Mock(**{'json.return_value': holidays})
print(response_mock.json())