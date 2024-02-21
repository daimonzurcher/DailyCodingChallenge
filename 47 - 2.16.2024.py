''' Problem Statement: Your mission is to write a function that partitions
an array into two sections: the first part containing all elements less than
a pivot value, and the second part containing all elements greater than or
equal to the pivot. The pivot should be the first element in the array.

Example: Input: [4, 2, 1, 5, 3] Output: [2, 1, 3, 4, 5] (4 is the pivot) 

Bonus Challenge: Can your function also return the final index of the pivot after partitioning? '''


# per the problem statement, creating two section of the array and then adding them together to get a final array

def partition(arr):
    section_one = [] # initialize left part of pivot
    section_two = [] # initialize right part of pivot
    final_array = [] # initialize final array

    # iterate through each number in input array
    for num in arr:
        # if less than pivot, place on left side
        if num < pivot:
            section_one.append(num)
        # if greater than or equal to pivot, place on right side
        else:
            section_two.append(num)
    
    # combine lists and return final list
    final_array = section_one + section_two

    # bonus challenge
    pivot_new_position = final_array.index(pivot)
    print("After partioning, the pivot's final index is", pivot_new_position)

    return final_array

# input in example
input = [4, 2, 1, 5, 3]

# set pivot to first element
pivot = input[0]

# put input array into function
output = partition(input)

# print result
print(output)