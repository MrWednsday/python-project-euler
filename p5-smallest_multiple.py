# 2520 is the smallest number that can be divided by each of the 
# numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible 
# by all of the numbers from 1 to 20?

def modDivision(number, divisor):
    return number % divisor == 0

def smallestMultiple():
    number = 20 * 2
    divide = list(range(1,21))
    found = False
    while not found:
        x = list(map(modDivision, [number] * 20, divide))
        found = all(x)
        if found:
            return number
        number += 10
    
print(smallestMultiple())