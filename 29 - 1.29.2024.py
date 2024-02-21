''' Problem Statement: Your task is to create a function that converts a given integer
into its binary representation and counts the number of consecutive 1's in the binary form.
Return this count as the output.

Example: Input: 13 Output: 2 (Since 13 in binary is 1101, which has two consecutive 1's)

Guidelines:

You can utilize any programming language.

Aim for a solution that is both efficient and easy to understand.

Bonus Challenge: Extend your function to handle negative numbers as well. '''

# use Python's 'bin' function in order to handle negative numbers as well

# function to count consecutive ones
def count_consecutive_ones(num):
    binary_rep = bin(num)[2:] # something new I learned! Python puts '0b' in front of binary numbers so you need to slice this out
    max_consecutive_ones = 0 # initialize max
    current_consecutive_ones = 0 # initialize current

    # for loop that iterates through each character in the binary number and counts number of 1s in succession; stores max value and resets count to zero if bit isn't a '1'
    for bit in binary_rep:
        if bit == '1':
            current_consecutive_ones += 1
            max_consecutive_ones = max(max_consecutive_ones, current_consecutive_ones)
        else:
            current_consecutive_ones = 0
        
    return max_consecutive_ones

# get user input and store a value for the binary so users can see the binary of their entered number
user_input = int(input("Enter a number to be evaluated: "))
user_input_binary = bin(user_input)[2:]

# store result from the function count_consecutive_ones() and print output to user
result = count_consecutive_ones(user_input)
print("Your input of", user_input, "is", user_input_binary, "in binary.", result, "consecutive 1s appear in the result.")