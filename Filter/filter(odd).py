# Print odd numbers using filter() 

def is_odd(n):
    return n % 2 != 0
nums = [2,6,4,8,7,9,2,0]
odds = list(filter(is_odd, nums))
print(odds)



