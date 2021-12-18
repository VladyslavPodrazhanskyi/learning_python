from unittest.mock import Mock

# Create a mock object

my_mock = Mock()

# create arbitrary attributes on the fly (return also Mock instance)
# attribute (field)
print(my_mock.some_attribure)
# method (can be without arguments or accept any number of arguments)
print(my_mock.some_method('sfj'))

'''
Mock instances 
store data on how you used them. 
For instance, you can see if you called a method, 
how you called the method
'''

json = Mock()

json.loads('{"key": "value"}')


# You know that you called loads() so you can
# make assertions to test that expectation

json.loads.assert_called()
json.loads.assert_called_once()
json.loads.assert_called_with('{"key": "value"}')
json.loads.assert_called_once_with('{"key": "value"}')
print(json.loads.call_count)
print(json.loads.call_args_list)




#     json.loads('{"key": "value"}')
#    <Mock name='mock.loads()' id='4550144184'