''' Problem Statement: Given an NxN grid, your task is to
write a function that places lights on the grid in such a way
that every row, column, and diagonal is illuminated, using the
minimum number of lights. Assume each light illuminates its row,
column, and diagonals fully regardless of distance.

Example: For a simple 3x3 grid, find the minimum number of lights 
needed and their positions to illuminate the whole grid. 

Challenge yourself: Can you find a pattern or formula for the minimum
lights needed as the grid size increases?'''

# function to calculate the total num of rows, cols, diagonals
def min_lights_needed(n):
    total_lines = 2 * n - 1

    return n + total_lines

# get user input for grid size and print result
grid_size = int(input("Enter grid size (N x N): "))
lights_needed = min_lights_needed(grid_size)
print("Minimum number of lights needed for a", grid_size, "x", grid_size, "grid: ", lights_needed)