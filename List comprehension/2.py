# What is lambda in Python?
# Lambda is a function that is defined without a name.
# Usually in python functions are defined with a keyword def but anonymous functions are defined by the keyword lambda.
# The lambda function is used along with the built-in function map(), filter().

# Example:
# we can see how to find the cube of a given number using lambda function.
cube = lambda a: a * a * a
print(cube(5))



# Python Lambda function using filter():
# In this example, I have taken a list of numbers and assigned the values from 1 to 12 in it.
# The filter() function is called with all the items in the list and returns a new list.
# And then we can use the lambda function using the filter() to get the multiples of 4 from the list.
number = [1,2,3,5,4,6,8,9,11,12]
multiples_of_4 = list(filter(lambda a: (a%4 == 0) ,number))
print(multiples_of_4)



# Python Lambda function using map():
# In this example, I have taken a name of list as numbers and assigned multiples of 5 and each number is divided by 5 using map().
# The map() is called with all the items in the list and a new list is returned.
number = [5,10,15,20,25,30,35,40,45,50]
newnumber = list(map(lambda c: c/5 ,number))
print(newnumber)



# Python list comprehension lambda closure:
# used to create resource globally and reuse it in a function to avoid performance issues.
# used only in nested functions.
# When we call the lambda function it will take the ‘_’ value from the closed namespace.
# It will not take the ‘_’ value when the lambda object is created. ‘_’ value lives in the namespace.
# In this example, I have used c = [_() for _ in b]. It works here because a new namespace is used for all the names except the original input.
# In b = [lambda: _ for _ in a] here I have used different names for loop target.we are not masking over the closed over name.
# ‘_’ value remains in the namescope and returns the value 4 for 4 times.
a = [1, 2, 3 , 4]
b = [lambda: _ for _ in a]
c = [_() for _ in b]
print(a)
print(b)
print(c)