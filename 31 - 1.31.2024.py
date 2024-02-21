''' Problem Statement: You are given an unsorted array of integers. Your task is to write a function that sorts the array in ascending order. However, the twist is to optimize the sorting algorithm for the best possible time complexity.

Example: Input: [34, 7, 23, 32, 5, 62] Output: [5, 7, 23, 32, 34, 62]

Guidelines:

Feel free to use any programming language.

Consider different sorting algorithms and their efficiencies.

Bonus Challenge: Can you sort the array in-place without using extra space? '''

# After reviewing some notes from a previous CS course, I think that using a Merge Sort would work well here
#   Merge Sort has a time complexity of O(n log n) ; "divide and conquer"-esque approach
#       Merge sort involves repeatedly dividing into halves until individual elements are considered, then merging the sorted halves

def merge_sort(arr):
    # check if array has more than one element - base case for recursion
    if len(arr) > 1:
        # find middle index of the array
        middle = len(arr) // 2
        # split array into two halves
        left = arr[:middle]
        right = arr[middle:]

        # recursively sort left and right halves
        merge_sort(left)
        merge_sort(right)

        # merge the halves after sorted; initialize the left half, right half, array
        i = j = k = 0

        # compare left half and right half; merge into array
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        
        # check for remaining elements in left half
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        
        # check for remaining elements in right half
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

# allow user to input list (separated by spaces)
user_input = input("Enter a list of integers, separated by spaces please: ")
user_input_list = [int(num) for num in user_input.split()]

# put user's list through the merge sort function and print sorted list
merge_sort(user_input_list)
print("Sorted List: ", user_input_list)
