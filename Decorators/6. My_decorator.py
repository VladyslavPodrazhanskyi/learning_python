# Create a decorator manually.
# Decorator accepts function that we do not want to change and
# Change result of this function without change of the function
# with code before call of the function and after call of the function.

# 1. Decorator function is function that accept as parameter - NAME of function to decorate.
#defines wrapper function and returns NAME of wrapper function.


def my_decorator(unchangeable_function):

# 2 Body of function-decorator consist of 2 parts:

#2.1. Description of wrapper function(its have no parameters)
    def wrapper_func():
# it's bodyconsists of 3 parts:
        print("I do it before call the secret_function")  # 1. Code before call of the functio to decorate.
        unchangeable_function()                           # 2. Call the function to decorate
        print("I do it after call the secret function")   # 3. Code after call of the functio to decorate.
#2.2. Returns NAME of wrapper_func
    return wrapper_func

# 3. Description of function to be decorated.
def my_function():
    print("This is the function that I am decorating!")

# 4. Test: call the function to be decorated
print("\n")
my_function()   # Result: This is the function that I am decorating!
print("\n")
# 5. Create Var that returns NAME of my_decorated function
name_of_my_decorated_function = my_decorator(my_function)
# 5.1. I call function my_decorator and put NAME of my_function as an argument.
# 5.2. Decorator function defines wrapper_function that after call fulfill
# 3 parts: code before, call my_function and code after.
# 5.3. Decorator function returns NAME or wrapper_function

# 6. I call inner wrapper function throug outer decoration function (see sample 3. Two functions...)
# received result of callin my function with code before and code after.
name_of_my_decorated_function()

# 7. Переименуем имя нашей функции в функцию-декоратора от нашей функции:
# итогда при вызове нашей функции мы вызываем декорируемую функцию.
# ЭТО ТО, ЧТО И ДЕЛАЕТ ДЕКОРАТОР
print("\n")
my_function = my_decorator(my_function)
my_function()
print("\n")
# Используем язык декораторов.
@my_decorator
# @my_decorator эквивалентно коду -  my_new_function = my_decorator(my_new_function)
def my_newfunction():
    print("Do NOT change me!!!")

my_newfunction()