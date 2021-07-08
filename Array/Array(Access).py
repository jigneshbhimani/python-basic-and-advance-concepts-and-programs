# Accessing elements from the Array:

# To access the array items refer to the index number.
# Use the index operator [ ] to access an item in a array.
# The index must be an integer.

import array as arr

a = arr.array('i', [1, 2, 3, 4, 5, 6])
print("Access element is: ", a[0])
print("Access element is: ", a[3])


b = arr.array('d', [2.5, 3.2, 3.3])
print("Access element is: ", b[1])
print("Access element is: ", b[2])
