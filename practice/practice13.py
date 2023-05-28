from decimal import Decimal


def float_to_decimal(number: float) -> Decimal:
    # return Decimal(str(number))
    return Decimal(number)


print(float_to_decimal(5.34))
print(type(float_to_decimal(5.34)))

words = [
    {'word': "w1"},
    {'word': "w2"},
    {'word': "w3"},
]

print([word for word in words if word.get('word', '') == 'w2'][0].get('word'))

# todo: analyze dynamical import
# try:
#     module = importlib.import_module(__name__)
#     strategy = getattr(module, strategy_name)
#     return strategy()
# except AttributeError as e:
#     logging.error(e)
#     raise NotImplementedError(f'The {strategy_name} was not implemented')