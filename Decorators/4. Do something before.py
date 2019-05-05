def say_hello():
    print("Hello!")


f = say_hello


del say_hello


# Pаз мы можем возвращать функцию, значит, мы можем и передавать её другой функции, как параметр:

def do_something_before(function):
    print("I do somethin before call function")
    function()

do_something_before(f)