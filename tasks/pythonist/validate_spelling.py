"""
https://pythonist.ru/po-bukvam/
"""


def validate_spelling(txt: str) -> bool:
    list_txt = txt.lower().split('. ')
    return ''.join(list_txt[:-1]) == ''.join(char for char in list_txt[-1] if char.isalpha())


assert validate_spelling("C. Y. T. O. P. L. A. S. M. Cytoplasm?")
assert validate_spelling("P. H. A. R. A. O. H. Pharaoh!")
assert not validate_spelling("H. A. N. K. E. R. C. H. E. I. F. Handkerchief.")
