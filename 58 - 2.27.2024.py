''' Problem Statement: Implement a depth-first search algorithm to traverse a tree or graph structure.
Your task is to write a function that explores nodes or vertices deeply before moving on to neighbors,
aiming to visit every node in the structure.

Example Scenario: Given a tree or graph, start at a selected node and explore as far as possible
along each branch before backtracking.

Guidelines:

You may choose any programming language for your implementation.

Emphasize on creating a clear and efficient recursive DFS function.

Bonus Challenge: Extend your DFS to solve a specific problem, such as finding a path in a maze
or evaluating expressions stored in a tree structure. '''

# DFS for traversing a graph structure

from collections import defaultdict

# create class for the graph
class Graph:
    # initialize graph - using defaultdict
    def __init__(self):
        self.graph = defaultdict(list)

    # function to add an edge from u to v
    def add_edge(self, u, v):
        self.graph[u].append(v)

    # function to mark current vertex as visited; print it
    def dfs_util(self, v, visited):
        visited.add(v)
        print(v, end=" ")

        # for all vertices adjacent (neighbors), recur function
        for neighbor in self.graph[v]:
            if neighbor not in visited:
                self.dfs_util(neighbor, visited)

    # create a set for tracking vertices that have been visited
    def dfs(self, start_vertex):
        visited = set()

        # call recursive utility function to perform DFS
        self.dfs_util(start_vertex, visited)

# example
graph = Graph()

# add edges to graph
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 2)
graph.add_edge(2, 0)
graph.add_edge(2, 3)
graph.add_edge(3, 3)

print("Depth First Traversal (starting from vertex 2):")

# perform DFS starting from vertex 2
graph.dfs(2)