# Chaining Decorators means decorating a function with multiple decorators.

def decorator(func):
	def deco():
		x = func()
		return x * x
	return deco

def decorator1(func):
	def deco():
		x = func()
		return 2 * x
	return deco

@decorator              # Route1
@decorator1             # Route2
def num():
	return 10

print(num())

# calling the function as 
# decorator(decorator1(num))
