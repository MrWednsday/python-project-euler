# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143?
import math

number = 600851475143

def largestPrimeFactor(n):
    largestPrime = 0
    if n % 2 == 0:
        largestPrime = 2
    else:
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            while n % i == 0:
                largestPrime = i
                n = n / i
    return largestPrime



print(largestPrimeFactor(number))