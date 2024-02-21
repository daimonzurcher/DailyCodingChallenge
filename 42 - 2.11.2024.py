''' Problem Statement: Given a directed graph with weights and two vertices,
write a function that computes the shortest path from the start vertex to
the end vertex. The graph will be represented as a list of edges with their weights.

Example: Graph represented as edges: [(A, B, 1), (B, C, 2), (A, C, 4)]
Start Vertex: A End Vertex: C Output: Shortest Path = A -> B -> C with a total weight of 3

Guidelines:

Any programming language is welcome.

Consider using Dijkstra's algorithm, Bellman-Ford, or any other algorithm you find suitable.

Bonus: Can your solution efficiently handle negative weights? '''

# I learned about Dijkstra's algorithm in an undergrad course in Spring of 2020...
# Needless to say I needed a refresher before tackling this problem...

import heapq

def dijkstra(graph, start, end):
    # initialize distances from start vertex to all other vertices as infinity
    distances = {vertex: float('inf') for vertex in graph}
    # distance from start to itself is 0
    distances[start] = 0
    
    # initialize heap with (distance, vertex) tuples
    heap = [(0, start)]
    heapq.heapify(heap)
    
    # initialize dict to keep track of previous vertices in the shortest path
    previous_vertices = {vertex: None for vertex in graph}
    
    while heap:
        current_distance, current_vertex = heapq.heappop(heap)
        
        # if current vertex is the end vertex, we found the shortest path
        if current_vertex == end:
            path = []
            while current_vertex is not None:
                path.append(current_vertex)
                current_vertex = previous_vertices[current_vertex]
            # reverse path to get it in the correct order (from start to end)
            return path[::-1], current_distance
        
        # otherwise, explore neighbors of current vertex
        if current_vertex in graph:
            for neighbor, weight in graph[current_vertex].items():
                distance = current_distance + weight
                # if we found a shorter path to the neighbor, update distance and previous vertex
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous_vertices[neighbor] = current_vertex
                    heapq.heappush(heap, (distance, neighbor))
    
    # if we reach here, no path from start to end
    return None, float('inf')

# graph represented as edges (from example)
edges = [('A', 'B', 1), ('B', 'C', 2), ('A', 'C', 4)]
# convert edges to adjacency list representation
graph = {}
for edge in edges:
    start, end, weight = edge
    if start not in graph:
        graph[start] = {}
    if end not in graph:
        graph[end] = {}  # Add this line to account for all vertices
    graph[start][end] = weight

# start and end vertices
start_vertex = 'A'
end_vertex = 'C'

# find the shortest path and its weight
shortest_path, total_weight = dijkstra(graph, start_vertex, end_vertex)
if shortest_path:
    # print the shortest path and its total weight
    print("Shortest Path =", ' -> '.join(shortest_path), "with a total weight of", total_weight)
else:
    print("No path exists from", start_vertex, "to", end_vertex)