''' Problem Statement: Your goal is to write a program that finds the shortest path
through a maze from a starting point (S) to the finish (F). The maze is represented
as a 2D array, where 0s are open paths, and 1s are walls. You can move up, down, left,
or right but cannot move diagonally.

Example Maze:

[
[1, 1, 1, 1, 1, 1, 1],
[1, 0, 0, 0, 1, 0, 1],
[1, 0, 1, 0, 0, 0, 1],
[1, 0, 1, 1, 1, 0, 1],
[1, S, 1, 0, F, 0, 1],
[1, 1, 1, 1, 1, 1, 1]
]

Guidelines:

Implement your solution in any programming language.

Consider using Breadth-First Search (BFS) or Depth-First Search (DFS) for pathfinding.

Bonus Points: Can your solution handle mazes with multiple solutions by finding the absolute shortest path? '''

from collections import deque

def shortest_path_maze(maze):
    if not maze:
        return []

    # define directions, order is as follows: up, down, left, right
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    # find the starting point (S)
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == 'S':
                start = (i, j)
                break

    # initialize queue for BFS
    queue = deque([(start, 0)])  # (position, distance)
    visited = set()  # set to keep track of visited positions

    # perform Breadth-First Search (BFS)
    while queue:
        (x, y), distance = queue.popleft()

        # check if we reached the finish (F)
        if maze[x][y] == 'F':
            return distance

        # explore neighbors
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            # check if neighbor is within bounds and not a wall
            if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]) and maze[nx][ny] != '1' and (nx, ny) not in visited:
                queue.append(((nx, ny), distance + 1))
                visited.add((nx, ny))

    # if no path found
    return -1

# maze given in example
maze = [
    [1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1],
    [1, 'S', 1, 0, 'F', 0, 1],
    [1, 1, 1, 1, 1, 1, 1]
]

# use function to find the shortest path
shortest_path_length = shortest_path_maze(maze)
print("Length of the shortest path:", shortest_path_length)