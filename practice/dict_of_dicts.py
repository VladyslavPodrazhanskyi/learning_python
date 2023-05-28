list_of_dicts = [
    {
        'vehicle': '3498284',
        "trim": {
            'trim_name': 'some_trim',
            'trim_id': '394829048'
        }
    },
    {
        'vehicle': '832874',
        "trim": {
            'trim_name': 'other_trim',
        }
    },
]

print(list_of_dicts[1].get('trim').get('trim_id'))