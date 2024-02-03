''' Problem Statement: Write a function that uses recursion to find the nth number
    in the Fibonacci sequence. Remember, the Fibonacci sequence is a series of numbers
    where each number is the sum of the two preceding ones, usually starting with 0 and 1.

Example: Input: n = 5 Output: 5 (The sequence is 0, 1, 1, 2, 3, 5)

Guidelines:

Choose any programming language you're comfortable with.

Pay special attention to the efficiency of your recursive solution.

Challenge: Can you prevent stack overflow for large values of n? '''

# The solution is working, but I haven't figured out how to do the "challenge"
#   of preventing stack overflow for large values of n...

# Fibonacci function
def fibonacci_recursion(n):
    # base cases: Fibonacci sequence always starts with 0 and 1
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    # recursion - sum of the two previous numbers
    return fibonacci_recursion(n - 1) + fibonacci_recursion(n - 2)

# get user input
num = int(input("Enter a number, n, to find the n-th number in the Fibonacci sequence: "))

# put user's number into the function
result = fibonacci_recursion(num)

# print result
print(f"The {num}-th Fibonacci number is: {result}")
