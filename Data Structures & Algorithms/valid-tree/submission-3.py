class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #map to store neighbors of node
        neighbors = {}
        for i in range(n):
            neighbors[i] = []
        
        for edge in edges:
            neighbors[edge[0]].append(edge[1])
            #undirected graph
            neighbors[edge[1]].append(edge[0]) 
        


        #dfs cycle detection
            #used set
            #edge case: can't DFS back to the parent
        visited = set()
        def dfs(node, parent):
            if node in visited:
                return False
            
            visited.add(node)

            for neighbor in neighbors[node]:
                if neighbor == parent:
                    continue
                if not dfs(neighbor, node):
                    return False
            
            return True
        x = dfs(0, None)
        if len(visited) -1 != n-1: 
            print(len(visited))
            return False #unconnected
        return x
        