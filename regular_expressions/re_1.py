import re

str1 = 'foo123bar'

print('123' in str1) # True
print(str1.find('123')) # 3
print(str1.index('123')) # 3

# re.search(<regex>, <string>)
# Scans a string for a regex match
# If a match is found, then re.search() returns a match object.
# Otherwise, it returns None.

print(re.search('123', str1))     # <re.Match object; span=(3, 6), match='123'>
# span: '123' = str1[3:6]
print(re.search('123456', str1))  # None

# metacharacters
# character class = set of characters inside []
print(re.search('[0-9][0-9][0-9]', str1)) # <re.Match object; span=(3, 6)

# . - any character excep a new line
print(re.search('1.3', str1))
print(re.search('1.3', 'foo13bor'))  # None

# ^ - match at the start of a string
# Complements a character class

