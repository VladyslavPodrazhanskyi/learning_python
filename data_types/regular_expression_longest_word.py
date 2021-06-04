import re

def longest_word(s):
    set_dividers = {char for char in s if not char.isalnum()}
    str_dividers = '[' + ''.join(set_dividers) + ']'
    word_list = re.split(str_dividers, s)
    max_len = max(map(len, word_list))
    longest_words = filter(lambda x: len(x) == max_len, word_list)
    return next(longest_words)

print(longest_word('k k k k k 2398489    rt&'))
