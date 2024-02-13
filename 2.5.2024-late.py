''' Problem Statement: Write a function that generates the Fibonacci sequence
    up to the nth number. However, there's a catch - your function should also
    identify the first Fibonacci number in the sequence that is divisible by a given integer x.

Example: Input: n = 10, x = 4 Output: Sequence: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34], First divisible by 4: 8 '''

# need to loop to generate through 'n' Fibonacci numbers, and check each one for divisibility by 'x'

def fibonacci_and_divis(n, x):
    # initialize Fibonacci sequence with first two numbers
    sequence = [0, 1]

    # iterate to generate Fibonacci numbers, up to 'n'th number
    while len(sequence) < n:
        # calc next Fibonacci number by adding the last two numbers
        next_num = sequence[-1] + sequence[-2]
        # append the next Fibonacci number to sequence
        sequence.append(next_num)
        # check if next Fibonacci number is divisible by 'x' - if yes, return the sequence and the number
        if next_num % x == 0:
            return sequence, next_num
    
    # if loop exits with no number divisible by 'x', just return sequence
    return sequence, None

# get user inputs for 'n' and 'x'
n = int(input("Enter the value of n - n represents the number to which the Fibonacci sequence will be generated: "))
x = int(input("Enter the value of x - x represents the number to determine divisibility: "))

# call function with user inputs
fibonacci_sequence, first_divisible = fibonacci_and_divis(n, x)

# print results
print("Sequence:", fibonacci_sequence)
if first_divisible is not None:
    print("First divisible by", x, ":", first_divisible)
else:
    print("No Fibonacci number in the sequence is divisible by", x)