# Print even number using filter()

def is_even(n):
    return n % 2 == 0
nums = [2,6,4,8,7,9,2,0]
evens = list(filter(is_even, nums))
print(evens)