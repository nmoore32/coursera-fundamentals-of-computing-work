##
# Create a list containing the first 6 prime numbers in ascending order.
# Print out the 2nd, 4th, and 6th numbers in the list.
#
from math import sqrt


def is_prime(n):
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


primes = []
for num in range(2, 101):
    if is_prime(num):
        primes.append(num)

print(f"{primes[1]} {primes[3]} {primes[5]}")
