''' Problem Statement: Implement a sorting algorithm that not only sorts an
array of integers efficiently but also demonstrates your understanding of algorithm
optimization and elegance. Whether you choose Merge Sort, Quick Sort, Heap Sort, or
even an algorithm of your own invention, the goal is to sort with style.
'''

# choosing merge sort for this challenge
def merge_sort(arr):
    # base case: if array has one (or zero) elements, already sorted
    if len(arr) <= 1:
        return arr
    
    # divide array into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    # recursively sort each half
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    
    # merge sorted halves
    return merge(left_half, right_half)

def merge(left, right):
    # initialize empty list to store merged array
    merged = []
    # initialize left and right indices
    left_index = right_index = 0
    
    # merge the two sorted arrays
    while left_index < len(left) and right_index < len(right):
        # if element in left array is smaller, append to merged array
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        # if element in right array is smaller, append to merged array
        else:
            merged.append(right[right_index])
            right_index += 1
    
    # add any remaining elements from left and right arrays
    merged.extend(left[left_index:])
    merged.extend(right[right_index:])
    
    # returned merged array
    return merged

# test merge sort algorithm with made up example
arr = [12, 11, 13, 5, 6, 7]
sorted_arr = merge_sort(arr)
print("Sorted array:", sorted_arr)