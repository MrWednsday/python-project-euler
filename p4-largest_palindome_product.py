# A palindromic number reads the same both ways. 
# The largest palindrome made from the product of 
# two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product 
# of two 3-digit numbers.

def largestPalindomeNumber():
    largestPalindorme = 0
    for i in range(999, 99, -1):
        for j in range(999, 99, -1):
            if checkIfPalnidrome(i * j):
                if i * j > largestPalindorme:
                    largestPalindorme = i * j
    
    return largestPalindorme

def checkIfPalnidrome(number):
    text = str(number)
    return text[::-1][0 : int(len(text) / 2)] == text[0 : int(len(text) / 2)]

print(largestPalindomeNumber())
