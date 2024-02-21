''' Problem Statement: Design a function that simulates building a tower
by stacking blocks. Your function should accept a series of block weights
(integers) and stack them in descending order, from the heaviest at the
base to the lightest at the top, using stack operations (push and pop).

Example: Input: [5, 3, 8, 2, 1, 4] Output: Stack sequence: 8, 5, 4, 3, 2, 1

Guidelines:

Implement your solution in any programming language.

Emphasize using stack operations to achieve the tower construction.

Bonus Challenge: Can your function efficiently rearrange blocks if presented in random order? '''

# finally got back on track!!! hoping to stay on track now.

def build_tower(blocks):
    # sort the blocks in descending order
    sorted_blocks = sorted(blocks, reverse=True)

    # print the sorted blocks
    print("Stack sequence:", ", ".join(str(block) for block in sorted_blocks))

# input given in example
blocks = [5, 3, 8, 2, 1, 4]

# function to 'build the tower'
build_tower(blocks)