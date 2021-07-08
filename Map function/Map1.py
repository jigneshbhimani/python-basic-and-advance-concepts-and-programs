# Definition and Usage:

# The map() function executes a specified function for each item in an iterable.
# The item is sent to the function as a parameter.

# Syntax:
'''
map(function, iterables)
'''
# function: Required. The function to execute for each item.
# iterable: Required. A sequence, collection or an iterator object.
# You can send as many iterables as you like, just make sure the function has one parameterfor each iterable.



# Make new fruits by sending two iterable objects into the function:
def myfunc1(a, b):
  return a + b

x = map(myfunc1, ('apple', 'banana', 'cherry'), (' orange', ' lemon', ' pineapple'))

print(x)

#convert the map into a list, for readability:
print(list(x))