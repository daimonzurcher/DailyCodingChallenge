''' Problem Statement: You need to write a function that takes a number n as an input and returns a staircase of 'n' steps made of hash (#) characters and spaces. The last line must have no spaces, and each step should have one more hash than the last.

Example: Input: n = 4 Output:

arduinoCopy code
" #" " ##" " ###" "####" '''

# Obviously a little late to this, getting help up from 2.3.2024 to 2.12.2024... will work on getting back on track!

# need to iterate from 1 to 'n' steps, and print each step as needed

def staircase(n):
    # iterate from 1 to n to create each step
    for step_num in range(1, n + 1):
        # calc number of spaces and hashes for current step
        spaces = ' ' * (n - step_num)
        hashes = '#' * step_num
        # print step with the right number of spaces and hashes
        print(spaces + hashes)

# get user input for number of steps
user_input = int(input("Enter number of steps: "))

# call function w/ user input
staircase(user_input)