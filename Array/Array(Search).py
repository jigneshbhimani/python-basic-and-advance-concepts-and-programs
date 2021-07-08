# Searching element in a Array:

# To search an element in the array we use a python in-built index() method.
# This function returns the index of the first occurrence of value mentioned in arguments.


import array
arr = array.array('i', [1, 2, 3, 1, 2, 5])
print ("The new created array is : ", end ="")
for i in range (0, 6):
	print (arr[i], end =" ")
print ("\r")

# using index() to print index of 1st occurrenece of 2
print ("The index of 1st occurrence of 2 is : ", end ="")
print (arr.index(2))

# using index() to print index of 1st occurrenece of 1
print ("The index of 1st occurrence of 1 is : ", end ="")
print (arr.index(1))
