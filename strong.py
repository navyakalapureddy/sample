import math

def is_strong_number(num):
    """
    Checks if a given number is a strong number.
    A strong number is a number where the sum of the factorial of its digits
    equals the number itself.
    """
    original_num = num
    sum_of_factorials = 0
    
    # Handle the case of 0 separately as 0! is 1.
    if num == 0:
        return False # Strong numbers are typically positive integers.

    while num > 0:
        digit = num % 10
        sum_of_factorials += math.factorial(digit)
        num //= 10
    
    return sum_of_factorials == original_num

def find_strong_numbers_in_range(start, end):
    """
    Finds all strong numbers within a specified range (inclusive).
    """
    strong_numbers = []
    for i in range(start, end + 1):
        if is_strong_number(i):
            strong_numbers.append(i)
    return strong_numbers

# Find strong numbers between 1 and 5000
strong_numbers_found = find_strong_numbers_in_range(1, 5000)
print(f"Strong numbers between 1 and 5000 are: {strong_numbers_found}")