# Python cells and multi-scoped variables

# The value of the message variable is shared between two scopes of:
# 1.The say function.
# 2.The closure

# The label message is in two different scopes.
# However, they always reference the same string object with the value 'Hello'.

# Python creates an intermediary object called a cell.

def say():
    greeting = 'Hello'
    print(hex(id(greeting)))
    def display():
        print(hex(id(greeting)))
        print(greeting)
    return display
fn = say()
fn()
# To find the memory address of the cell object, you can use the __closure__ property
print(fn.__closure__)
# The __closure__ returns a tuple of cells.
