"""
https://pythonist.ru/samoe-dlinnoe-slovo/
"""

from typing import List


def longest_word(sentence: str) -> str:
    # word_list = sentence.split()
    # longest = word_list[0]
    # for word in word_list[1:]:
    #     if len(word) > len(longest):
    #         longest = word
    # return longest
    return(max(sentence.split(), key=len))




assert longest_word("Margaret's toy is a pretty doll.") == "Margaret's"
assert longest_word("A thing of beauty is a joy forever.") == "forever."
assert longest_word("Forgetfulness is by all means powerless!") == "Forgetfulness"
