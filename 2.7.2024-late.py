''' Problem Statement: Develop a function that takes an array
    of integers and returns a new array containing only the unique
    elements from the original array. Ensure your solution efficiently handles large datasets.

Example: Input: [1, 2, 2, 3, 4, 4, 5] Output: [1, 3, 5] '''

def unique(arr):
    # initialize dict to store count of each element
    element_count = {}
    
    # count occurrences of each element in input array
    for num in arr:
        element_count[num] = element_count.get(num, 0) + 1

    # initialize empty list to store unique elements
    unique_list = []

    # iterate through input array
    for num in arr:
        # if element is unique, add it to unique list
        if element_count[num] == 1:
            unique_list.append(num)
    
    return unique_list

# test function with given example
input = [1, 2, 2, 3, 4, 4, 5]
output = unique(input)
print(output)