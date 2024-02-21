''' Problem Statement: Create a function that takes a 2D array representing a maze. Your function should determine if there's a path from the entrance (top-left corner) to the exit (bottom-right corner). The maze is composed of 0s (pathways) and 1s (walls). Your goal is to find a path through the maze if one exists.

Example: Input:

maze = [ [0, 1, 0, 0], [0, 1, 0, 1], [0, 0, 0, 0], [1, 0, 1, 0] ]

Output: True (A path exists from the top-left corner to the bottom-right corner) '''

# function to check if the move is within the boundaries, the cell is not a wall, and not visited
def is_valid_move(maze, row, col, visited):
    return 0 <= row < len(maze) and 0 <= col < len(maze[0]) and maze[row][col] == 0 and not visited[row][col]

# function to mark current cell as visited
def dfs(maze, row, col, visited):
    visited[row][col] = True

    # if at the exit, return True
    if row == len(maze) - 1 and col == len(maze[0]) - 1:
        return True
    
    # check all possible moves (up, down, left, right)
    moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for dr, dc in moves:
        new_row, new_col = row + dr, col + dc
        if is_valid_move(maze, new_row, new_col, visited):
            # recursion to explore the next cell
            if dfs(maze, new_row, new_col, visited):
                return True

    return False

# function to create a visited array - to keep track of visited cells
def has_path(maze):
    visited = [[False for _ in range(len(maze[0]))] for _ in range(len(maze))]
    
    # start DFS from the entrance (which is the top left corner)
    return dfs(maze, 0, 0, visited)

# test function with given example
maze = [
    [0, 1, 0, 0],
    [0, 1, 0, 1],
    [0, 0, 0, 0],
    [1, 0, 1, 0]
]
print(has_path(maze))