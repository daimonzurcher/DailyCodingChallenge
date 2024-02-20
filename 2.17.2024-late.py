''' Problem Statement: Develop an algorithm that finds the shortest path between
two points on a grid. This grid includes obstacles, represented as 1 (impassable terrain),
and open spaces, represented as 0 (passable terrain). Your algorithm should return the
path as a sequence of moves.

Example Grid:

[
[0, 0, 0, 1],
[1, 1, 0, 1],
[0, 0, 0, 0],
[0, 1, 1, 0]
]
Start: Top-left corner (0,0) End: Bottom-right corner (3,3)

Guidelines:

Implement your solution in any programming language.

Consider using algorithms like A* (A-star), Dijkstra, or BFS (Breadth-First Search) for optimal pathfinding.

Bonus Challenge: Can your solution handle dynamic changes in the grid? '''

# a previous challenge used BFS for an optimal pathfinding problem - we'll do the same here
#   BFS explores all possible paths from the start to the end, which guarantees the path found is the shortest

from collections import deque

def is_valid_move(grid, visited, row, col):
    # check if move is within the grid bounds and not blocked
    return 0 <= row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col] == 0 and not visited[row][col]

def bfs_shortest_path(grid, start, end):
    # direction definitions in this order: left, up, down, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # initialize visited array
    visited = [[False] * len(grid[0]) for _ in range(len(grid))]

    # initialize queue
    queue = deque([(start, [])])

    # mark start cell as visited
    visited[start[0]][start[1]] = True

    # BFS
    while queue:
        cell, path = queue.popleft()
        row, col = cell

        # check if reached the end
        if cell == end:
            return path + [cell] # return path from start to end
        
        # explore all neighboring cells that are valid
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if is_valid_move(grid, visited, new_row, new_col):
                # mark neighbor cell as visited and queue it
                visited[new_row][new_col] = True
                queue.append(((new_row, new_col), path + [cell]))

    # if no path found
    return None

# given example grid
grid = [
    [0, 0, 0, 1],
    [1, 1, 0, 1],
    [0, 0, 0, 0],
    [0, 1, 1, 0]
]

# start and end points
start = (0, 0)
end = (3, 3)

# find shortest path
shortest_path = bfs_shortest_path(grid, start, end)

# print result
if shortest_path:
    print("Shortest path:", shortest_path)
else:
    print("No path found")