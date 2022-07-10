"""
maketrans() method returns a mapping table
for translation usable for translate() method,
is a static method that creates a one to one mapping
of a character to its translation/replacement

maketrans() method takes 3 parameters:

x - If only one argument is supplied, it must be a dictionary.
The dictionary should contain a 1-to-1 mapping from a single character string
to its translation OR a Unicode number (97 for 'a') to its translation.

y - If two arguments are passed, it must be two strings with equal length.
Each character in the first string is a replacement to its corresponding index in the second string.
z - If three arguments are passed, each character in the third argument is mapped to None.

"""

dict_a = {"a": "123", "b": "456", "c": "789"}
string = "wuh"
print(string.maketrans(dict_a))  # ord() from key
# {97: '123', 98: '456', 99: '789'}  - for any string

# len(first) must be equal len(second)
print(string.maketrans('abc', 'def'))  # {97: 100, 98: 101, 99: 102}
# len(third) can be any size
print(string.maketrans('abc', 'def', 'ghjhi'))  # {97: 100, 98: 101, 99: 102, 103: None, 104: None, 105: None}
# third args set to None previus values of keys
print(string.maketrans('abc', 'def', 'abcds'))  # {97: None, 98: None, 99: None, 100: None, 115: None}

"""
The string translate() method returns a string 
where each character is mapped 
to its corresponding character in the translation table.
"""

txt = 'abcdefghiabc'

mapping = 'any string here'.maketrans(
    'abc',
    'xyz',
    'def',
)

# manual mapping must have key as ord('char'),
# value can be string with any len
manual_mapping = {
    97: None,
    98: 'python',
    99: 'java',
}

print('Original txt is:', txt)
print('Translated txt is:', txt.translate(mapping))
# Original txt is: abcdefghiabc
# Translated txt is: xyzghixyz

print('Translated txt is:', txt.translate(manual_mapping))
# Translated txt is: pythonjavadefghipythonjava