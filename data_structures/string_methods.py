my_str = 'skfjskfj kTTTTasfjk'
my_extra_string = my_str
print('my str: ', my_str)
print('len my str: ', len(my_str))
print([(v, i) for i, v in enumerate(my_extra_string)])

# lower(), upper()

print(my_str.capitalize())  # first word
print(my_str.swapcase())
print(my_str.title())  # all words


def full_name(first, last):
    return (first + " " + last).title()


print(full_name('dima', 'UDochkin'))
print(my_str.find('45'))
print(my_str.replace("TT", 'GG', 1).replace('G', "X"))
print(my_str.startswith('kf', 1))
print(my_str.count('TT'))

################################################################
##### Check type of symbols in string  #################################
############################################################

print('sjfw92ылЕЕЕЕоа393'.isalnum())  # True if only letter and numbers
print('check alpha')
print('sjkfsfлывоаООО'.isalpha())  # True if only letter
print('39482984'.isdigit())  # True if only numbers
print('sfkjjsd_skfj'.isidentifier())
print('sk 34jd'.islower())  # number  and spaces acceptable
print('TT87'.isupper())  # number  and spaces acceptable
print('  \n  '.isspace())
print('Tkfj Yer'.istitle())  # all words with title, numbers are NOT OK
# string.isprintable()


############################################################
############## String Formatting  ##########################
############################################################

print('skfd  sjf'.center(20, '+'))
print('skfd  sjf'.ljust(20, '+'))
print('skfd  sjf'.rjust(20, '+'))
# print('a\tbc'.expandtabs())
# print('a\tbc')

print('He said: "What\'s there? I replied - nothing!"')


############################################################
############## Translate  ###################################
############################################################

def swap_quotes(some_string: str) -> str:
    tr_dict = {ord("'"): ord('"'), ord('"'): ord("'")}
    some_string = some_string.translate(tr_dict)
    return some_string


my_str = 'Hello Tom!'
x = 'T'
y = 'S'
z = '!'

my_table = str.maketrans(x, y, z)

print(my_str.translate(my_table))