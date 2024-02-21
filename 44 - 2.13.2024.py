''' Problem Statement: Develop a function that identifies the longest increasing subsequence
within an array of integers. The subsequence must be strictly increasing, but the elements do
not need to be contiguous in the original array.

Example: Input: [0, 8, 4, 12, 2, 10, 6, 14, 1, 9]
Output: Length of the longest increasing subsequence = 4 (The sequence could be [0, 4, 10, 14] or [0, 2, 6, 9], etc.) '''

def longest_increasing_subsequence(nums):
    if not nums:
        return 0

    # initialize a list to store length of longest increasing subsequence ending at each index
    list = [1] * len(nums)

    # iterate through each index
    for i in range(1, len(nums)):
        # check all previous indices for increasing subsequences
        for j in range(i):
            if nums[i] > nums[j]:
                list[i] = max(list[i], list[j] + 1)

    # return the max value in list
    return max(list)

# input from example
nums = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9]
# use function to find length of the longest increasing subsequence
length = longest_increasing_subsequence(nums)
print("Length of the longest increasing subsequence =", length)