# A decorator is nothing but a function that takes a function to be decorated as its parameter, and returns a function.
# Functions are first class objects that means that functions in Python can be used or passed as arguments.
# Used to modify the behavior of function or class.
# functions are taken as the argument into another function and then called inside the wrapper function.


# without using Decorators
def div(a,b):
    if a < b:
        a,b = b,a
    print(a/b)
div(4,8)

# Using Decorators(function inside function)
def div(a,b):
    print(a/b)
def smart_div(func):
    def inner(a,b):
        if a<b:
            a,b = b,a
        return func(a,b)
    return inner
div = smart_div(div)
div(2,12)