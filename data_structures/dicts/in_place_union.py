payload = {
    'key1': 'value1',
    'key2': 'value2',
    'key3': 'value3',
}

case = {
    'case_key': 'case_value'
}

# |= - Perform in-place union
payload |= case

print(payload)


