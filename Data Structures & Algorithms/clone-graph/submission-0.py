"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        new_graph = {}

        def dfs(node):
            if node in new_graph:
                return new_graph[node]

            clonedCopy = Node(node.val)
            new_graph[node] = clonedCopy

            for nei in node.neighbors:
                clonedCopy.neighbors.append(dfs(nei))

            return clonedCopy

        return dfs(node) if node else None  