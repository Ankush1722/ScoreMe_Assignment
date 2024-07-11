"""
Assignment: Implement the most efficient algorithm to solve the given problem.

Problem Statement:
You are given a Directed Acyclic Graph (DAG) with `n` nodes, numbered from `0` to `n-1`.
The graph is represented as an adjacency list where `graph[i]` is a list of tuples `(j, w)`,
representing an edge from node `i` to node `j` with weight `w`. Your task is to find the longest
path in the graph starting from any node.

Function Signature:
def longest_path(graph: list) -> int:

Parameters:
- graph (list): A list of lists, where `graph[i]` contains tuples `(j, w)` representing an edge
  from node `i` to node `j` with weight `w`.

Returns:
- int: The length of the longest path in the graph.

Example:
>>> graph = [
...     [(1, 3), (2, 2)],
...     [(3, 4)],
...     [(3, 1)],
...     []
... ]
>>> longest_path(graph)
7
"""

def topological_sort(graph):
    n = len(graph)  # Get the number of nodes in the graph
    indegree = [0] * n  # Initialize the in-degree of each node to 0
    for node in range(n):  # Iterate over each node
        for neighbor, weight in graph[node]:  # Iterate over each neighbor of the current node
            indegree[neighbor] += 1  # Increment the in-degree of the neighbor

    topo_order = []  # List to store the topological order
    queue = [node for node in range(n) if indegree[node] == 0]  # Queue to store nodes with in-degree 0

    while queue:  # Process nodes in the queue
        node = queue.pop(0)  # Pop the first node from the queue
        topo_order.append(node)  # Add the node to the topological order
        for neighbor, weight in graph[node]:  # Iterate over each neighbor of the current node
            indegree[neighbor] -= 1  # Decrement the in-degree of the neighbor
            if indegree[neighbor] == 0:  # If the in-degree of the neighbor becomes 0
                queue.append(neighbor)  # Add the neighbor to the queue

    return topo_order  # Return the topological order

def longest_path(graph: list) -> int:
    topo_order = topological_sort(graph)  # Get the topological order of the graph
    n = len(graph)  # Get the number of nodes in the graph
    dp = [-float('inf')] * n  # Initialize the dp array with negative infinity
    dp[0] = 0  # Starting node with no incoming edges

    for node in topo_order:  # Iterate over each node in the topological order
        if dp[node] != -float('inf'):  # If the node is reachable
            for neighbor, weight in graph[node]:  # Iterate over each neighbor of the current node
                dp[neighbor] = max(dp[neighbor], dp[node] + weight)  # Update the dp value of the neighbor

    return max(dp)  # Return the maximum value in the dp array
