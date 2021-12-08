from col1.collections import namedtuple

Token = namedtuple("Token", ("addition", "multiplication"))
func_tuple = Token(lambda x, y: x + y, lambda x, y: x * y)
print(func_tuple.addition(5, 7))
print(func_tuple.multiplication(5, 7))











