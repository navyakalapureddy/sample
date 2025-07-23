import math

def is_prime(num):
    """
    Checks if a number is prime.
    A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.
    """
    if num <= 1:
        return False  # Numbers less than or equal to 1 are not prime
    # Check for divisibility from 2 up to the square root of the number
    # This optimization is based on the fact that if a number has a divisor greater than its square root,
    # it must also have a divisor smaller than its square root.
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False  # If divisible, it's not prime
    return True  # If no divisors found, it's prime

print("Prime numbers from 1 to 100 are:")
for number in range(1, 101):
    if is_prime(number):
        print(number)