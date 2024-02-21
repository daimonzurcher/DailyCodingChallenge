''' Problem Statement: Write a recursive function that calculates the nth number
in a specific sequence or solves a particular problem (e.g., factorial,
Fibonacci series, or traversing a nested structure). Choose a problem that best
showcases the beauty and efficiency of recursion.

Guidelines:

You can select any programming language for this task.

Ensure your recursive solution includes a base case to prevent infinite recursion.

Bonus Challenge: Optimize your recursion with techniques like memoization to enhance performance '''

# since we've done some stuff with the Fibonacci sequence already, let's work with calculating factorials this time

def factorial(n):
    # base case: factorial(0) = 1
    if n == 0:
        return 1
    else:
        # recursive case: factorial(n) = n * factorial(n - 1)
        return n * factorial(n - 1)

# get user input
n = int(input("Enter a number: "))

# print result
print("Factorial of {} = {}".format(n, factorial(n)))