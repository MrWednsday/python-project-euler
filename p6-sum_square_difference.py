# The sum of the squares of the first ten natural numbers is,
# The square of the sum of the first ten natural numbers is,
# Hence the difference between the sum of the squares of the 
# first ten natural numbers and the square of the sum is .
# Find the difference between the sum of the squares of the 
# first one hundred natural numbers and the square of the sum.

sumOfSquares = 0
numbers = range(1, 101, 1)

for x in numbers:
    sumOfSquares += x*x

x = sum(numbers)*sum(numbers) - sumOfSquares
print(x)