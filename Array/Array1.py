# An array is a collection of items stored at contiguous memory locations.
# To store multiple items of the same type together.
# It easier to calculate the position of each element by simply adding an offset to a base value.
# Array in Python can be created by importing array module.
# array(data_type, value_list) is used to create an array with data type and value list specified in its arguments.


# Creation of Array
import array as arr

# creating an array with integer type
a = arr.array('i', [1, 2, 3])
print ("The new created array is: ", end =" ")
for i in range (0, 3):
	print (a[i], end =" ")
print()

# creating an array with float type
b = arr.array('d', [2.5, 3.2, 3.3])
print ("The new created array is: ", end =" ")
for i in range (0, 3):
	print (b[i], end =" ")
	
