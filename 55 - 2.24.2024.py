''' Problem Statement: Write a function that finds the only unique element in an array where every other
element is repeated. Your solution should efficiently identify the unique number in a sea of duplicates.

Example: Input: [2, 3, 2, 4, 3, 4, 5] Output: 5 (5 is the only element that does not have a duplicate)

Guidelines:

Implement your solution in any programming language.

Aim for a solution that is both time-efficient and space-efficient.

Bonus Challenge: Can your algorithm handle a large array with minimal performance impact? '''

# XOR (exclusive or) operation would be huge here to handle large arrays with minimal performance impact

# function
def id_unique(arr):
    unique_element = 0 # initialize unique element variable to 0

    for num in arr:
        unique_element ^= num # XOR each element in array --> if we XOR a num with itself, result is 0 (so all duplicates will cancel each other out)

    return unique_element # return unique element

# given example test
arr = [2, 3, 2, 4, 3, 4, 5]

# print result
print(id_unique(arr))