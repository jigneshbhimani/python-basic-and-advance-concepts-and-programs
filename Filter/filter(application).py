# It is normally used with Lambda functions to separate list, tuple, or sets.



# a list contains both even and odd numbers.
from typing import Sequence
sequence = [0, 1, 2, 3, 5, 8, 13]

# result contains odd numbers of the list
result = filter(lambda x: x % 2 != 0, sequence)
print(list(result))

# result contains even numbers of the list
result = filter(lambda x: x % 2 == 0, sequence)
print(list(result))
