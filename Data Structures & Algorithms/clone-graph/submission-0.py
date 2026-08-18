"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        d = {}
        if not node:
            return node

        def dfs(node):
            if node in d: #we already added
                return d[node]
            
            copy = Node(node.val)
            d[node] = copy

            for neighbor in node.neighbors:
                copy.neighbors.append(dfs(neighbor))

            return copy


        print(d)
        
        return dfs(node)
        