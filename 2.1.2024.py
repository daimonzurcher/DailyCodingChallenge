''' Problem Statement: Create a function that rotates a given NxN matrix by 90 degrees clockwise.
    The challenge is to perform this rotation in-place, without using any extra space.

Example:
Input Matrix:

Copy code
1 2 3 4 5 6 7 8 9

Output Matrix:

Copy code
7 4 1 8 5 2 9 6 3

Guidelines:

Any programming language is welcome.

Focus on solving this in-place to maintain O(1) space complexity.

Think about how you can handle larger matrices '''

# O(1) complexity means rotating the matrix without using any additional memeroy that scales with the input size.
#   i.e., minimize the use of extra space by ensuring that the space required is constant [O(1)]

# Can't lie - this racked my brain a bit. Took a lot to visualize the matrix shifting and
# haven't had a lot of practice with matrices in Python. Also, I couldn't figure out how to
# get it to where the user could input the matrix dimensions and then the elements in the matrix,
# then have it rotate...


def rotate_matrix(input):
    matrix_length = len(input)

    # traverse each layer - start from outermost
    for layer in range(matrix_length // 2):
        first = layer
        last = matrix_length - 1 - layer

        # iterate through each element in current layer
        for i in range(first, last):
            offset = i - first

            # save top element
            top = input[first][i]

            # move left element to the top
            input[first][i] = input[last - offset][first]

            # move bottom element to the left
            input[last - offset][first] = input[last][last - offset]

            # move right element to the bottom
            input[last][last - offset] = input[i][last]

            # move top element to the right
            input[i][last] = top

# example provided
example_input = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# put example matrix into function
rotate_matrix(example_input)

# print rotated matrix
for row in example_input:
    print(row)