''' Problem Statement: You have an array of integers. Your task is to write a function that returns the highest product that can be obtained by multiplying any three numbers from the array.

Example: Input: array = [1, 10, 2, 6, 5, 3] Output: 300 (Because 10 6 5 = 300)

Guidelines:

Language: You can use any programming language of your choice.

Think about edge cases (What if the array contains negative numbers?).

Strive for efficient solutions. Can you do it in O(n) time complexity? '''

# I initially wrote this code just focusing on positive array elements. Trying to construct the function
# to incorporate what should happen if negative numbers are allowed was a bit trickier, but a lot of fun!

def highest_product(array):
    # assume we NEED at least three elements in the array
    if len(array) < 3:
        raise ValueError("Array needs at least three numbers.")
    
    # convert user input values from string to int
    array = [int(num) for num in array]
    
    # initialize variables - set bounds to +/- infinity
    max1 = float('-inf')
    max2 = float('-inf')
    max3 = float('-inf')
    min1 = float('inf')
    min2 = float('inf')
    
    # iterate through array to find largest AND smallest values
    for num in array:
        # update max values
        if num >= max1:
            max3 = max2
            max2 = max1
            max1 = num
        elif num >= max2:
            max3 = max2
            max2 = num
        elif num > max3:
            max3 = num

        # update min values
        if num <= min1:
            min2 = min1
            min1 = num
        elif num < min2:
            min2 = num

    # return max number, taking into consideration the double negative (equals large positive) potential
    return max(max1 * max2 * max3, min1 * min2 * max1)

# get user input
user_input_str = input("Enter an array of three or more numbers, separated by spaces: ")

# split user input into a list
user_input_list = user_input_str.split()

# put user array (now a list) into function
result = highest_product(user_input_list)

# print multiplication
print(result)