# What is Python list comprehension?
# used to create a new list based on the existing list.
# used to work on the list.
# returns the list and It contains expression and brackets.


# List comprehension Example:
# I have taken a list as chocolate and if condition is used.
# Here, the if condition is true. So it returned a new list.

chocolate = ["5star", "silk", "milkybar"]
newchocolate_list = [a for a in chocolate if "5" in a]
print(newchocolate_list)


# Now, we will check what happens if the items are not present in the list.
# Then, it will return an empty list because the if condition is not true.

chocolate = ["5star", "silk", "milkybar"]
newchocolate_list = [a for a in chocolate if "4" in a]
print(newchocolate_list)