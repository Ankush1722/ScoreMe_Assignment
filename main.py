### 2. `main.py`
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
    n = len(graph)
    indegree = [0] * n
    for node in range(n):
        for neighbor, weight in graph[node]:
            indegree[neighbor] += 1

    topo_order = []
    queue = [node for node in range(n) if indegree[node] == 0]

    while queue:
        node = queue.pop(0)
        topo_order.append(node)
        for neighbor, weight in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    return topo_order

def longest_path(graph: list) -> int:

    topo_order = topological_sort(graph)
    n = len(graph)
    dp = [-float('inf')] * n
    dp[0] = 0  # Starting node with no incoming edges

    for node in topo_order:
        if dp[node] != -float('inf'):  # If the node is reachable
            for neighbor, weight in graph[node]:
                dp[neighbor] = max(dp[neighbor], dp[node] + weight)

    return max(dp)

