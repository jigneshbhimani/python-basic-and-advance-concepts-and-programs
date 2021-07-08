# Updating Elements in a Array:

# To update an element in the array we simply reassign a new value to the desired index we want to update.


import array
arr = array.array('i', [1, 2, 3, 1, 2, 5])
print ("Array before updation : ", end ="")
for i in range (0, 6):
	print (arr[i], end =" ")
print ("\r")

# updating a element in a array
arr[2] = 6
print("Array after updation : ", end ="")
for i in range (0, 6):
	print (arr[i], end =" ")
print()

# updating a element in a array
arr[4] = 8
print("Array after updation : ", end ="")
for i in range (0, 6):
	print (arr[i], end =" ")
