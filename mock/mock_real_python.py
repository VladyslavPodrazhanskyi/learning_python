from unittest.mock import Mock

# Create a mock object
#
json = Mock()

json.loads('{"key": "value"}')

json.loads('{"key": "value"}')
json.loads('s = {"key": "value"}')
# You know that you called loads() so you can
# make assertions to test that expectation

# json.loads.assert_called()
# json.loads.assert_called_once()
# json.loads.assert_called_with('{"key": "value"}')
# json.loads.assert_called_once_with('{"key": "value"}')

print(json.loads.call_count)
print(json.loads.call_args_list)




#     json.loads('{"key": "value"}')
#    <Mock name='mock.loads()' id='4550144184'