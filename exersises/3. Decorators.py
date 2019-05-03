def mydecoratorfunction(some_function): # function to be decorated passed as argument
    def wrapper_function(): # wrap the some_function and extends its behaviour
        # write code to extend the behaviour of some_function()
        some_function() # call some_function
        return wrapper_function # return wrapper function