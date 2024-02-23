''' Problem Statement: Write a function that merges two sorted arrays into a single sorted array.
Your solution should efficiently blend both arrays into a new array that maintains sorted order
without using built-in sort functions.

Example: Array 1: [1, 3, 5] Array 2: [2, 4, 6] Output: [1, 2, 3, 4, 5, 6]

Guidelines:

Any programming language is welcome.

Aim for an optimal solution that minimizes time and space complexity.

Bonus Challenge: Adapt your function to handle merging of multiple sorted arrays. '''

def merge_sorted_arrays(arr1, arr2):
    # initialize indices for arr1 and arr2
    i = 0
    j = 0

    # initialize merged array
    merged_array = []

    # while elements in both input arrays still, merge
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged_array.append(arr1[i])
            i += 1 # increment arr1 here to compare its next index to arr2's current index
        else:
            merged_array.append(arr2[j])
            j += 1 # increment arr2 here to compare its next index to arr1's current index
    
    # check if arr1 has any remaining elements and append to merged array
    while i < len(arr1):
        merged_array.append(arr1[i])
        i += 1

    # check if arr2 has any remaining elements and append to merged array; in the example's case, this is necessary as once 5 from arr1 gets appended,
    # arr1 will be looped through and the first 'while' loop will exit (leaving 6 in arr2 to be remaining)
    while j < len(arr2):
        merged_array.append(arr2[j])
        j += 1

    return merged_array

# given example
arr1 = [1, 3, 5]
arr2 = [2, 4, 6]

# print result after putting input arrays into function
print(merge_sorted_arrays(arr1, arr2))